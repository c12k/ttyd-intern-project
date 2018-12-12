pipeline {
  agent any
  stages {
    stage('Start') {
      steps {
        slackSend(color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL}) of commit: https://github.com/cmcc13/ttyd-intern-project/commit/${env.GIT_COMMIT}")
      }
    }
    stage('Web rebuild') {
      steps {
        sh 'if docker ps | awk -v app=web_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop web_container; echo "web_container exists, removing it."; else echo "web_container does not exist already."; fi'
        sh 'docker build -f ./Dockerfileweb -t webstuff:latest .'
      }
    }
    stage('Postgres rebuild') {
      steps {
        sh 'if docker ps | awk -v app=postgres_docker \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop postgres_docker; echo "postgres_docker exists, removing it."; else echo "postgres_docker did not exist"; fi'
        sh 'docker pull postgres:11.1'
      }
    }
    stage('Rasa NLU rebuild') {
      steps {
        sh 'if docker ps | awk -v app=nlu_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop nlu_container; echo "nlu_container exists, removing it."; else echo "nlu_container did not exist"; fi'
        sh 'docker pull rasa/rasa_nlu:0.13.7-full'
        sh 'docker build -f ./Dockerfilenlu -t nluimage .'
      }
    }
    stage('Rasa Core rebuild') {
      steps {
        sh 'if docker ps | awk -v app=core_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop core_container; echo "core_container exists, removing it."; else echo "core_container did not exist"; fi'
        sh 'docker pull rasa/rasa_core:0.12.0'
        sh 'docker build -f ./Dockerfilecore -t coreimage .'
      }
    }
    stage('Setup for Tests') {
      steps {
        sh 'docker run -td -p 3000:3000 --rm --name web_container webstuff'
        sh 'docker run --rm --name postgres_docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v data:/var/lib/postgresql/data  postgres:11.1'
        sh 'docker run -d -p 5000:5000 --rm --name nlu_container nluimage'
        sh 'docker run -d -p 5005:5005 --rm --name core_container coreimage'
        sh 'docker network create --driver=bridge --subnet=172.28.0.0/16 --ip-range=172.28.5.0/24 jenkins_test_network'
        sh 'docker network connect --ip 172.28.5.1 jenkins_test_network web_container'
        sh 'docker network connect --ip 172.28.5.2 jenkins_test_network postgres_docker'
        sh 'docker network connect --ip 172.28.5.3 jenkins_test_network nlu_container'
        sh 'docker network connect --ip 172.28.5.4 jenkins_test_network core_container'
      }
    }
    stage('Testing') {
      agent {
      // Equivalent to "docker build -f Dockerfile --build-arg version=1.0.2 .
        dockerfile {
          filename 'Dockerfiletests'
          additionalBuildArgs  '--rm --network=jenkins_test_network'
          args '-p 80:80'
        }
      }
      steps {
        sh 'python ./devops/Test-scripts/web-tests/test_page_status_and_hello.py 172.28.5.1 3000'
        sh 'ls'
        sh 'python ./devops/Test-scripts/web-tests/test_nlu_page_status_and_hello.py 172.28.5.1 5000'
      }
    }
  }
  post {
    success {
      slackSend(color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL}) of commit: https://github.com/cmcc13/ttyd-intern-project/commit/${env.GIT_COMMIT}")

    }

    failure {
      slackSend(color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL}) of commit: https://github.com/cmcc13/ttyd-intern-project/commit/${env.GIT_COMMIT}")

    }

    cleanup {
      sh 'if docker ps | awk -v app=web_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop web_container; echo "web_container exists, removing it."; else echo "web_container does not exist already."; fi'
      sh 'if docker ps | awk -v app=postgres_docker \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop postgres_docker; echo "postgres_docker exists, removing it."; else echo "postgres_docker did not exist"; fi'
      sh 'if docker ps | awk -v app=nlu_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop nlu_container; echo "nlu_container exists, removing it."; else echo "nlu_container did not exist"; fi'
      sh 'if docker ps | awk -v app=core_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop core_container; echo "core_container exists, removing it."; else echo "core_container did not exist"; fi'
      sh 'docker network rm jenkins_test_network'
    }
  }
}