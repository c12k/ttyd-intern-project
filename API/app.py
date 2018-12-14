from flask import Flask, render_template, request, Response
from flask_cors import CORS
import requests
import json
import logging
import os
log = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# display the default form index.html
# and handle the posting of the form to test call API's
# based on fields on the form (url, text)
@app.route('/', methods=['GET', 'POST'])
def index():
    msg = "test message"
    url = "localhost:3000"
    responsemsg= None
    if request.method == 'POST' and 'msg' in request.form:
        msg = request.form['msg']
    if request.method == 'POST' and 'url' in request.form:
        url = request.form['url']

    if request.method == 'POST':
        if 'getAPI' in request.form:
            if msg == None:
                msg = "test message"
            log.info('== Calling get')
            try:
                resp = requests.get(url, msg)
                if(resp.ok):
                    data = json.loads(resp.content)
                    log.info('== Response {}'.format(data))
                    if len(data) > 0:
                        responsemsg = data[0]['text']
                else:
                    responsemsg = 'empty response'
            except requests.exceptions.RequestException as e:
                log.info('== Error {}'.format(e))
                responsemsg = 'error {}'.format(e)
        if 'postAPI' in request.form:
            h = {"Content-Type": "application/json"}
            if msg ==None:
                msg = "test message"
            d = json.dumps({'sender': 'me', 'message': msg})
            log.info('== Calling with {}'.format(d))
            try:
                resp = requests.post(url, data=d, headers=h)
                if(resp.ok):
                    data = json.loads(resp.content)
                    log.info('== Response {}'.format(data))
                    if len(data) > 0:
                        responsemsg = data[0]['text']
                else:
                    responsemsg = 'empty response'
            except requests.exceptions.RequestException as e:
                log.info('== Error {}'.format(e))
                responsemsg = 'error {}'.format(e)
    return render_template('index.html', responsemsg=responsemsg)


@app.route('/health', methods=['GET'])
def health():
    msg = 'API app is healthy ok.'
    return render_template('index.html', responsemsg=msg)

# some simple API's that can be called from other programs
@app.route('/api1', methods=['GET'])
def api1():
    msg = 'API 1 is working.'
    return msg

@app.route('/api2', methods=['GET'])
def api2():
    msg = 'API 2 is working.'
    return msg

@app.route('/api3', methods=['POST'])
def api3():
    msg = 'API 3 POST call is working.'
    return msg

if __name__ == "__main__":
    handler = logging.StreamHandler()
    formatter = logging.Formatter( '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('== web app running.')
    app.run("0.0.0.0", port=80)
