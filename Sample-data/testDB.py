#!/usr/bin/python
# test python access to postgres DB
import pandas as pd
import psycopg2


def config():
    dbconfig = "host='localhost' user='' password='' dbname='ttyd' port=5432"
    return dbconfig


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # get connection parameters
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(params)
        cur = conn.cursor()
        cur.execute( 'select * from txn group by invoicedate order by invoicedate;')
        inv = pd.DataFrame(cur.fetchall())
        print(inv)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
