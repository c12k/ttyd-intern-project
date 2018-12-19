from flask import Flask, render_template, request, Response
from flask_cors import CORS
import requests
import json
import logging
import os
import datetime

log = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app)


def callmsgapi(uid, msg):
    url = "http://172.28.5.3:5005/webhooks/rest/webhook"
    h = {"Content-Type": "application/json"}
    if uid == None:
        uid = "me"
    if msg == None:
        msg = "hello"
    d = json.dumps({'sender': uid, 'message': msg})
    log.info('== Calling with {}'.format(d))
    try:
        resp = requests.post(url, data=d, headers=h)
    except Exception as e:
        log.info('== Error {}'.format(e))
        return 'Error calling API {}'.format(e)
    if(resp.ok):
        data = json.loads(resp.content)
        log.info('== Response {}'.format(data))
        if len(data) > 0:
            msgout = data[0]['text']
        else:
            msgout = 'empty response'
    else:
        log.info('== Error {}'.format(resp.text))
        return 'Error calling API {}'.format(resp.text)
    return msgout

@app.route('/', methods=['GET'])
def index():
    msg = None
    return render_template('index.html', responsemsg=msg)

@app.route('/', methods=['POST'])
def callnlp():
    msg = 'user: {}'.format(request.form['message'])
    msgs.append(msg)
    respmsg = callmsgapi(request.form['uid'], request.form['message'])
    t = '{0:%H:%M:%S}'.format(datetime.datetime.now())
    msg = 'Response: {} {}'.format(t,respmsg)
    msgs.append(msg)
    return render_template('index.html', responsemsg=msgs)

@app.route('/health', methods=['GET'])
def health():
    msg = 'chat API app is healthy ok.'
    return render_template('index.html', responsemsg=msg)

if __name__ == "__main__":
    handler = logging.StreamHandler()
    formatter = logging.Formatter( '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('== chat app running.')
    msgs = []
    app.run("0.0.0.0", port=80)
