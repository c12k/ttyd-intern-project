pipeline {
agent any
  stages {
    stage ('Start') {
      steps {
        // send build started notifications
        slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL}) of commit: https://github.com/cmcc13/ttyd-intern-project/commit/${env.GIT_COMMIT}")
      }
    }
    stage ('Web rebuild') {
        steps {
            //Stop and remove the old web_container if it exists.
            sh 'if docker ps | awk -v app=web_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop web_container; echo "web_container exists, removing it."; else echo "web_container does not exist already."; fi'
            //Rebuild the image
            sh 'docker build -f ./Dockerfileweb -t webstuff:latest .'
            //Run the image and throw exception if it fails
            sh 'docker run -td -p 3000:3000 --rm --name web_container webstuff'
        }
    }
    stage ('Postgres rebuild') {
        steps {
            //Stop and remove the old postgres_docker if it exists.
            sh 'if docker ps | awk -v app=postgres_docker \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop postgres_docker; echo "postgres_docker exists, removing it."; else echo "postgres_docker did not exist"; fi'
            //Pull the postgres 11.1 image
            sh 'docker pull postgres:11.1'
            //Run the image and throw exception if it fails
            sh 'docker run --rm --name postgres_docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v data:/var/lib/postgresql/data  postgres:11.1'
        }
    }
    stage ('Rasa NLU rebuild') {
        steps {
            //Stop and remove the old nlu_container if it exists.
            sh 'if docker ps | awk -v app=nlu_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop nlu_container; echo "nlu_container exists, removing it."; else echo "nlu_container did not exist"; fi'
            //Pull the rasa_nlu 0.13.7 image
            sh 'docker pull rasa/rasa_nlu:0.13.7-full'
            //Rebuild the image
            sh 'docker build -f ./Dockerfilenlu -t nluimage .'
            //Run the image and throw exception if it fails
            sh 'docker run -d -p 5000:5000 --rm --name nlu_container nluimage'
        }
    }
    stage ('Rasa Core rebuild') {
        steps {
            //Stop and remove the old nlu_container if it exists.
            sh 'if docker ps | awk -v app=core_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop core_container; echo "core_container exists, removing it."; else echo "core_container did not exist"; fi'
            //Pull the core 0.12.0 image
            sh 'docker pull rasa/rasa_core:0.12.0'
            //Rebuild the image
            sh 'docker build -f ./Dockerfilecore -t coreimage .'
            //Run the image and throw exception if it fails
            sh 'docker run -d -p 5005:5005 --rm --name core_container coreimage'
        }
    }
  }
  post {
    success {
      slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL}) of commit: https://github.com/cmcc13/ttyd-intern-project/commit/${env.GIT_COMMIT}")
    }

    failure {
      slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL}) of commit: https://github.com/cmcc13/ttyd-intern-project/commit/${env.GIT_COMMIT}")
    }
  }
}