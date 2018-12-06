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
        //Stop and remove the old web_container
        try {
                sh 'docker stop web_container'
                sh 'docker rm web_container'
        }
        catch (exc) {
             echo 'No preexisting web_container'
        }
        //Rebuild the image
        sh 'docker build -f ./Dockerfileweb -t webstuff:latest .'
        //Run the image and throw exception if it fails
        try {
                sh 'docker run -it --rm --name web_container webstuff'
        }
        catch (exc) {
             echo 'Error running web_container'
             throw}
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