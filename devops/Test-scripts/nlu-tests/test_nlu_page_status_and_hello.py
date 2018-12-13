"""Testing the nlu_container web page status code and content.

:param str arg1: The docker-machine IP address
:param int arg2: The port exposed for nlu_container

"""
import sys
import http.client
connection = http.client.HTTPConnection(sys.argv[1], sys.argv[2])
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
if (response.status != 200):
    raise Exception("The page status is not 200 Ok")
else:
    exit(0)
