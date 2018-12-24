# Devops Objective: Enable devops pipeline
Key results in 30 days:
- Repeatable Docker/Kubernetes cloud build on GKE
- Deployment files and pipelines for multiple python containers with external access and REST api’s between containers
- Build pipeline works for JS website calling Python backend
- Triggered build from Github to deployment
- Github repo showing all code with regular commits and documentation

# General notes
Current version of Rasa Core being used doesn't work on CPUs without AVX support.

# running jenkins in docker
docker run \
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins_container \
  jenkinsci/blueocean
  
  # Starting ELK stack in docker
  docker pull down from
  - docker.elastic.co/beats/filebeat:6.5.2
  - docker.elastic.co/logstash/logstash:6.5.2
  - docker.elastic.co/elasticsearch/elasticsearch:6.5.2
  - docker.elastic.co/kibana/kibana:6.5.2
  
  Build the custom images, filebeatimage and logstashimage, with Dockerfilefilebeat and Dockerfilelogstash.
  - docker build -f Dockerfilefilebeat -t filebeatimage .
  - docker build -f Dockerfilelogstash -t logstashimage .
  
  These put filebeat.yml and logstash.conf into the containers in the right places.
  
  
  Elasticsearch requires more than 1GB of RAM so increase the memory if using a VM and run these commands if you need to (the first is for those using docker-toolbox):
  - docker-machine ssh
  - sudo sysctl -w vm.max_map_count=262144
  
  
  Start the ELK stack with:
  - docker-compose -f docker-compose-elk.yml up
  
  This creates a network that filebeat and other containers will need to join.
  
  To send container logs to logstash, run containers with these arguments added to the docker run command:
  
  --network=ttyd-intern-project_default --log-driver=gelf --log-opt gelf-address=udp://172.21.0.7:5044
  
  
  Where the logstash IP is what you get from inspecting the ttyd-internp-roject_default network for logstash. Working on making this static.
  
  Start jenkins_container using the section above and if successful, run filebeat with:
  - docker run --rm --name filebeat_container --volumes-from jenkins_container:ro --network=ttydinternproject_default filebeatimage
  
  # Connecting Jenkins to Google Cloud
  Pull google/cloud-sdk
Then do:
docker run --rm -ti -v /.config/gcloud:/root/.config/gcloud google/cloud-sdk gcloud init

From then on, should start with default config which is already set up.

Yet another container we have going, would be more efficient to just add gcloud commands to the Jenkins image.

Plexiform is Daniel's google cloud project, this can be changed and probably should be for each user.
This is hardcoded only in the Jenkinsfile so replace plexiform-leaf-226104 everywhere in that with the project selected in the gcloud init step.

Jenkins then interacts with gcloud through the google/cloud-sdk docker image.
Images are tagged with gcr.io/plexiform-leaf-226104/IMAGENAME:latest when built by jenkins.
When the Deploy section is reached, gcloud authenticates docker and pushes these tagged images to the gcr.io repo.
Kubectl on gcloud then can pull them from the gcr.io repo when it needs those images.
Clusters should be created manually (maybe the current cluster name can be passed in as an env var?).
