from io import StringIO
from flask import Flask, render_template, request, Response
from flask_cors import CORS
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

import requests
import json
import logging
import os
log = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


def config():
    # assumes postgres is running, uses root access to then run DDL to create db.
    # the host IP comes from the docker network running postgres and this app.
    dbconfig = "host='172.23.0.2' user='postgres' password='' dbname='' port=5432"
    return dbconfig

# display the default form index.html
# and load a csv file and save to db
# buiuld API's to allow call from node.js
@app.route('/', methods=['GET', 'POST'])
def index():
    msg= None
    return render_template('uploadcsv.html', responsemsg=msg)


@app.route('/health', methods=['GET'])
def health():
    msg = 'API app is healthy ok.'
    return render_template('uploadcsv.html', responsemsg=msg)


@app.route('/loaddb', methods=['POST'])
def loaddb():

    # get csv filename from form
    if not ('csvfile' in request.form):
        msg = 'no csv file to load'
        return render_template('uploadcsv.html', responsemsg=msg)
    filename = request.form['csvfile']
    log.info('== loadcsv')

    # load csv file to dataframe
    try:
        df = pd.read_csv(filename)
    except IOError as e:
        log.info('== Error {}'.format(e))
        msg = 'error {}'.format(e)
        return render_template('uploadcsv.html', responsemsg=msg)
    log.info('df rows {}'.format(df.shape[0]))
    log.info('df head {}'.format(df.head(2)))

    # load data into db
    conn = None
    # get connection parameters
    params = config()
    log.info('== Connecting to the PostgreSQL database...')
    try:
        conn = psycopg2.connect(params)
        conn.autocommit = True # ensure we can drop and recreate db
        cur = conn.cursor()
        log.info('== create DB DDL')
        cur.execute('DROP DATABASE IF EXISTS retail;')
        cur.execute('CREATE DATABASE retail;')
        cur.execute('DROP TABLE IF EXISTS txn;')
        cur.execute('DROP DATABASE IF EXISTS retail;')
        log.info('== stream dataframe')

        # stream the data to csv to upload to DB (CSV faster than sql inserts)
        output = StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.getvalue()
        # jump to start of stream
        output.seek(0)
        log.info('== now load data to db')

        eng = create_engine(params)  # TODO - fails here on parms
        connection = eng.raw_connection()
        cursor = connection.cursor()
        # null values become ''
        cursor.copy_from(output, 'txn', null="", columns=(df.columns))

        log.info('== now run select')
        cur.execute('select * from txn limit(10);')
        inv = pd.DataFrame(cur.fetchall())
        log.info(inv)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        log.info(error)
        msg = error
        return render_template('uploadcsv.html', responsemsg=msg, csvfile=filename)
    finally:
        if conn is not None:
            conn.close()
            log.info('Database connection closed.')
    msg = 'Loaded {} rows; 2 sample rows follow \n {}'.format( df.shape[0], df.head(2))
    return render_template('uploadcsv.html', responsemsg=msg, csvfile=filename)


if __name__ == "__main__":
    handler = logging.StreamHandler()
    formatter = logging.Formatter( '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('== web app running.')
    app.run("0.0.0.0", port=80)
