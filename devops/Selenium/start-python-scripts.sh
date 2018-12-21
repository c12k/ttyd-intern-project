#!/usr/bin/env bash
#
# set -e
echo "Starting python test scripts"
python3 test_web_page_selenium_pytest.py
WEBEXIT=$?
python3 test_nlu_page_selenium_pytest.py
NLUEXIT=$?
python3 test_web_page_sign_up.py
SIGNUPEXIT=$?
python3 test_data_api.py
DATAEXIT=$?
python3 test_chat_api.py
CHATEXIT=$?
# If any of the test scripts failed, exit with an error
if [ $WEBEXIT -ne 0 ] || [ $NLUEXIT -ne 0 ] || [ $SIGNUPEXIT -ne 0 ] || [ $DATAEXIT -ne 0 ] || [ $CHATEXIT -ne 0 ];
then
    exit 1
else
    exit 0
fi