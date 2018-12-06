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
            sh 'app=web_container'
            sh 'if docker ps | awk -v app="$app" 'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}'; then docker stop "$app"; fi'
            //Rebuild the image
            sh 'docker build -f ./Dockerfileweb -t webstuff:latest .'
            //Run the image and throw exception if it fails
            sh 'docker run -it --rm --name web_container webstuff'
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