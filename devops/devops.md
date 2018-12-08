# Devops Objective: Enable devops pipeline
Key results in 30 days:
- Repeatable Docker/Kubernetes cloud build on GKE
- Deployment files and pipelines for multiple python containers with external access and REST api’s between containers
- Build pipeline works for JS website calling Python backend
- Triggered build from Github to deployment
- Github repo showing all code with regular commits and documentation

# running jenkins in docker
docker run \
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean