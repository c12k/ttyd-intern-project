#!/bin/bash
set -e
exec python test_nlu_page_status_and_hello.py "${@:1}" 5000
exec python test_page_status_and_hello.py "${@:1}" 3000
