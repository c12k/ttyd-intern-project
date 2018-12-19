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


def callmsgapi(msg):
    t = '{0:%H:%M:%S}'.format(datetime.datetime.now())
    response = t + " blah blah"
    return response

@app.route('/', methods=['GET'])
def index():
    msg = None
    return render_template('index.html', responsemsg=msg)

@app.route('/', methods=['POST'])
def callnlp():
    reqmsg = "{'" + request.form['uid'] + "' , '" + request.form['message'] + "'}"
    msg =  'user: {}'.format(reqmsg)
    msgs.append(msg)
    respmsg = callmsgapi(msg)
    msg = 'Response: {}'.format(respmsg)
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
