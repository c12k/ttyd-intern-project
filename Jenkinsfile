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
            sh 'docker run -td --rm --name web_container webstuff'
        }
    }
    stage ('Postgres rebuild') {
        steps {
            //Stop and remove the old web_container if it exists.
            sh 'if docker ps | awk -v app=postgres_docker \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop postgres_docker; echo "postgres_docker exists, removing it."; else echo "postgres_docker did not exist"; fi'
            //Pull the postgres 11.1 image
            sh 'docker pull postgres:11.1'
            //Run the image and throw exception if it fails
            sh 'docker run --rm --name postgres_docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v data:/var/lib/postgresql/data  postgres:11.1'
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