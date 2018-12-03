#!/bin/bash
set -e
function print_help {
    echo "Available options:"
    echo " interact - Start Rasa Core interactive"
    echo " serve - Start Rasa Core server"
    echo " debug - Start Rasa Core server with debug"
    echo " trainnlu - Train language model"
    echo " trainchat - Train the dialogue model"
    echo " help  - Print this help"
    echo " run   - Run an arbitrary command inside the container"
}

case ${1} in
    interact)
        exec python -m rasa_core.run -d ./dialogue -u ./nlu --endpoints endpoints.yml "${@:2}"
        ;;
    serve)
        exec python -m rasa_core.run -d ./dialogue --enable_api --endpoints endpoints.yml --nlu ai2/v1 --port 5005 --cors "*" --credentials credentials.yml
        ;;
    debug)
        exec python -m rasa_core.run -d ./dialogue --debug --enable_api --response_log logs --endpoints endpoints.yml --nlu ai2/v1 --port 5005 --cors "*" --credentials credentials.yml
        ;;
    run)
        exec "${@:2}"
        ;;
    trainnlu)
        exec python -m rasa_nlu.train -c train_nlu_config.yml -d data/training.json -o ./nlu --fixed_model_name="v1" --project ai2
        ;;
    trainchat)
        exec python -m rasa_core.train -s ./data/stories.md -d ./domain.yml -o ./dialogue -c core-config.yml
        ;;
    *)
        print_help
        ;;
esac