# ttyd-intern-project
This project is split into 3 components.  A website that provides login/security and the ability to upload versions of a spreadsheet and the graphing and visualisation of that data.  A nlp processing component that handle text chat interface to do Q&A against the uploaded data.  and lastly a devops pipeline to build and deploy these components through containers (docker and kubernetes) to local laptop or google cloud.

Learning objectives include:
* learn GitFlow
* Learn teamwork across modules in a project

- Website
* should be responsive
* feature should include signup, login, load csv file, view file, graph file
* should be written in Javascript, nodeJS, HTML, CSS

- NLP
* should use Rasa_NLU and RASA_CORE as the engine
* needs to be trained on financial terminology eg simple chart of accounts terms
* should be able to handle questions like "show my revenue for the last 3 months"
* should be able to return generated text as well as graph images
* coding needs to be in Python 3

- devops
* should use docker and kubernetes
* code should be in python 3
* the build pipeline should be separate to the deployment pipeline
* the eslastic stack should be built into the pipeline
* the RASA containers should be built into the pipeline
* triggers from Git to run the pipeline should be automated