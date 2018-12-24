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
        sh 'docker build -f ./Dockerfileweb -t webimage:latest .'
      }
    }
    stage('Data rebuild') {
      steps {
        sh 'if docker ps | awk -v app=data_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop data_container; echo "data_container exists, removing it."; else echo "data_container did not exist"; fi'
        sh 'docker build -f ./Dockerfiledata -t dataimage .'
      }
    }
    stage('Chat rebuild') {
      steps {
        sh 'if docker ps | awk -v app=chat_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop chat_container; echo "chat_container exists, removing it."; else echo "chat_container did not exist"; fi'
        sh 'docker build -f ./Dockerfilechat -t chatimage .'
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
    stage('Deploy'){
      steps{
      withCredentials([file(credentialsId: "${env.JENKINS_GCLOUD_CRED_ID}", variable: 'JENKINSGCLOUDCREDENTIAL')])
      {
        sh """
          gcloud auth activate-service-account --key-file=${JENKINSGCLOUDCREDENTIAL}
          gcloud config set compute/zone asia-southeast1-a
          gcloud config set compute/region asia-southeast1
          gcloud config set project plexiform-leaf-226104
          kubectl --version
          //gcloud container clusters get-credentials ${GCLOUD_K8S_CLUSTER_NAME}
          c//hmod +x $BASE_DIR/k8s/process_files.sh
          //cd $BASE_DIR/k8s/
          //./process_files.sh "$GCLOUD_PROJECT_ID" "${IMAGE_NAME}" "${DOCKER_PROJECT_NAMESPACE}/${IMAGE_NAME}:${RELEASE_TAG}" "./${IMAGE_NAME}/"
          //cd $BASE_DIR/k8s/${IMAGE_NAME}/.
          //kubectl apply -f $BASE_DIR/k8s/${IMAGE_NAME}/
          //gcloud auth revoke --all
          """
      }
      }
    }
    stage('Setup for Tests') {
      steps {
        // Run all the containers
        sh 'docker run -td -p 3000:3000 --rm --name web_container webimage'
        sh 'docker run -d -p 80:80 --rm --name data_container dataimage'
        sh 'docker run -d -p 5000:5000 --rm --name nlu_container nluimage'
        sh 'docker run -d -p 5005:5005 --rm --name core_container coreimage'
        sh 'docker run -d -p 8081:80 --rm --name chat_container chatimage'
        // Create a network and connect the images to it (core container only if it still exists)
        sh 'docker network create --driver=bridge --subnet=172.28.0.0/16 --ip-range=172.28.5.0/24 jenkins_test_network'
        sh 'docker network connect --ip 172.28.5.1 jenkins_test_network web_container'
        sh 'docker network connect --ip 172.28.5.2 jenkins_test_network data_container'
        sh 'docker network connect --ip 172.28.5.3 jenkins_test_network nlu_container'
        sh 'docker network connect --ip 172.28.5.4 jenkins_test_network core_container'
        sh 'docker network connect --ip 172.28.5.5 jenkins_test_network chat_container'
        // sh 'if docker ps | awk -v app=core_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker network connect --ip 172.28.5.4 jenkins_test_network core_container; echo "core_container exists, adding to network."; else echo "core_container did not exist"; fi'
        // Rebuild the test image
        sh 'docker build -f Dockerfileselpy -t selpyimage .'
      }
    }
    stage('Testing') {
      steps {
        sh 'docker run --rm --name selpy_container --network=jenkins_test_network selpyimage'
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
      // Disconnect all containers from the test network and remove the network
      sh 'if docker ps | awk -v app=web_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop web_container; echo "web_container exists, removing it."; else echo "web_container does not exist already."; fi'
      sh 'if docker ps | awk -v app=data_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop data_container; echo "data_container exists, removing it."; else echo "data_container did not exist"; fi'
      sh 'if docker ps | awk -v app=nlu_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop nlu_container; echo "nlu_container exists, removing it."; else echo "nlu_container did not exist"; fi'
      sh 'if docker ps | awk -v app=core_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop core_container; echo "core_container exists, removing it."; else echo "core_container did not exist"; fi'
      sh 'if docker ps | awk -v app=chat_container \'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}\'; then docker stop chat_container; echo "chat_container exists, removing it."; else echo "chat_container did not exist"; fi'
      sh 'docker network rm jenkins_test_network'
    }
  }
}
