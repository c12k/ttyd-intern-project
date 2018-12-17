from flask import Flask, render_template, request, Response
from flask_cors import CORS
import pandas as pd
import requests
import json
import logging
import os
log = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# display the default form index.html
# and load a csv file and save to db
# buiuld API's to allow call from node.js
@app.route('/', methods=['GET', 'POST'])
def index():
    msg = "test message"
    responsemsg= None
    return render_template('uploadcsv.html', responsemsg=responsemsg)


@app.route('/health', methods=['GET'])
def health():
    msg = 'API app is healthy ok.'
    return render_template('uploadcsv.html', responsemsg=msg)


@app.route('/testcsv', methods=['POST'])
def testcsv():
    msg = 'test csv.'
    if 'csvfile' in request.form:
        filename = request.form['csvfile']
        log.info('== loadcsv')
        try:
            df = pd.read_csv(filename)
        except IOError as e:
            log.info('== Error {}'.format(e))
            msg = 'error {}'.format(e)
            return render_template('uploadcsv.html', responsemsg=msg)
        log.info('df rows {}'.format(df.shape[0]))
        log.info('df head {}'.format(df.head(2)))
        msg = 'Loaded {} rows; 2 sample rows follow \n {}'.format( df.shape[0], df.head(2))
    return render_template('uploadcsv.html', responsemsg=msg)


@app.route('/loaddb', methods=['POST'])
def loaddb():
    msg = 'loaddb.'
    return render_template('uploadcsv.html', responsemsg=msg)


if __name__ == "__main__":
    handler = logging.StreamHandler()
    formatter = logging.Formatter( '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('== web app running.')
    app.run("0.0.0.0", port=80)
