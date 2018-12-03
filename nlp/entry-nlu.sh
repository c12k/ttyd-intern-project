#!/bin/bash
set -e
function print_help {
    echo "Available options:"
    echo " start - Start NLU server"
    echo " debug - Start NLU server with debug"
    echo " train - train model"
    echo " help  - Print this help"
    echo " run   - Run an arbitrary command inside the container"
}

case ${1} in
    start)
        exec python -m rasa_nlu.server --path projects --pre_load ai2/v1
        ;;
    debug)
        exec python -m rasa_nlu.server --debug --path projects --response_log logs
        ;;
    train)
        exec python -m rasa_nlu.train -c app/train_nlu_config.yml -d app/training.json -o projects --fixed_model_name="v2" --project ai2
        ;;
    run)
        exec "${@:2}"
        ;;
    *)
        print_help
        ;;
esac