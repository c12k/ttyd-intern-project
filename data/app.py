from flask import Flask, render_template, request, Response
from flask_cors import CORS
import requests
import json
import logging
import os
import pandas as pd

log = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app)

def init():
    filename = "Retail.csv"
    log.info('== loadcsv')
    # load csv file to dataframe
    try:
        df = pd.read_csv(filename)
    except IOError as e:
        log.info('== Error {}'.format(e))
        msg = 'error {}'.format(e)
        return render_template('index.html', responsemsg=msg)
    log.info('df rows {}'.format(df.shape[0]))
    log.info('df head {}'.format(df.head(2)))
    return df


def gettxnbyCountry(ctry='Australia'):
    log.info('== get tot country')
    a = df[df.Country.isin([ctry])]
    b = a.Quantity*a.UnitPrice
    tot = b.sum()
    msg = 'Total sales for {} is {}'.format(ctry, tot)
    return msg


def gettxnbyCustomer(cust=17850):
    log.info('== get cust')
    a = df[df.CustomerID==cust]
    b = a.Quantity*a.UnitPrice
    tot = b.sum()
    msg = 'Total sales for customer {} is {}'.format(cust, tot)
    msg += '\n first rows \n{}'.format(a.head(5))
    return msg


def gettxnbyProduct(prod='22727'):
    log.info('== get product')
    a = df[df.StockCode==prod]
    b = a.Quantity*a.UnitPrice
    tot = b.sum()
    msg = 'Total sales for product {} is {}'.format(prod, tot)
    msg += '\n first rows \n{}'.format(a.head(5))
    return msg

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = msg = 'csv loaded, {} rows'.format(
        df.shape[0]) + '\n sample rows: \n {}'.format(df.head(2))
    return render_template('index.html', responsemsg=msg)

@app.route('/health', methods=['GET'])
def health():
    msg = 'data API app is healthy ok.'
    return render_template('index.html', responsemsg=msg)

@app.route('/init', methods=['POST'])
def api1():
    df = init()
    msg = 'csv loaded, {} rows'.format(
        df.shape[0]) + '\n sample rows: \n {}'.format(df.head(2))
    return render_template('index.html', responsemsg=msg)

@app.route('/listCust', methods=['POST'])
def api2():
    msg = gettxnbyCustomer()
    return render_template('index.html', responsemsg=msg)


@app.route('/listProd', methods=['POST'])
def api3():
    msg = gettxnbyProduct()
    return render_template('index.html', responsemsg=msg)


@app.route('/listTotal', methods=['POST'])
def api4():
    msg = gettxnbyCountry()
    return render_template('index.html', responsemsg=msg)

if __name__ == "__main__":
    handler = logging.StreamHandler()
    formatter = logging.Formatter( '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.info('== web app running.')
    df = init()
    app.run("0.0.0.0", port=80)
