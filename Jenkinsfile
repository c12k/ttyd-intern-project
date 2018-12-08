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
        sh 'docker run -td -p 3000:3000 --rm --name web_container webstuff'
      }
    }
    stage('Postgres rebuild') {
      steps {
        sh 'if docker ps | awk -v app=postgres_docker \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop postgres_docker; echo "postgres_docker exists, removing it."; else echo "postgres_docker did not exist"; fi'
        sh 'docker pull postgres:11.1'
        sh 'docker run --rm --name postgres_docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v data:/var/lib/postgresql/data  postgres:11.1'
      }
    }
    stage('Rasa NLU rebuild') {
      steps {
        sh 'if docker ps | awk -v app=nlu_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop nlu_container; echo "nlu_container exists, removing it."; else echo "nlu_container did not exist"; fi'
        sh 'docker pull rasa/rasa_nlu:0.13.7-full'
        sh 'docker build -f ./Dockerfilenlu -t nluimage .'
        sh 'docker run -d -p 5000:5000 --rm --name nlu_container nluimage'
      }
    }
    stage('Rasa Core rebuild') {
      steps {
        sh 'if docker ps | awk -v app=core_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop core_container; echo "core_container exists, removing it."; else echo "core_container did not exist"; fi'
        sh 'docker pull rasa/rasa_core:0.12.0'
        sh 'docker build -f ./Dockerfilecore -t coreimage .'
        sh 'docker run -d -p 5005:5005 --rm --name core_container coreimage'
      }
    }
    stage('Testing') {
      steps {
        sh 'python "./devops/Test scripts/web tests/test_page_status_and_hello.py" "localhost" 3000'
        sh 'python "./devops/Test scripts/nlu tests/test_nlu_page_status_and_hello.py" "localhost" 5000'
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

  }
}