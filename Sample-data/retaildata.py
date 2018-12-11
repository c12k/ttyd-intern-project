#! /usr/bin/env python3

import sys
import psycopg2
import psycopg2.extras
from calendar import Calendar

CONNSTRING = "dbname=ttyd"


def fetch_month_data(year, month):
    "Fetch a month of data from the database"
    date = "%d-%02d-01" % (year, month)
    sql = """
  select invoicedate as date, sum(quantity) as volume, sum(unitprice*quantity) as dollars
    from txn
   where invoicedate >= date %s
     and invoicedate  < date %s + interval '1 month'
     group by invoicedate
order by invoicedate;
"""
    pgconn = psycopg2.connect(CONNSTRING)
    curs = pgconn.cursor()
    curs.execute(sql, (date, date))

    res = {}
    for (date, volume, dollars) in curs.fetchall():
        res[date] = (volume, dollars)

    return res


def list_for_month(year, month):
    """List all days for given month, and for each
    day list fact book entry.
    """
    data = fetch_month_data(year, month)

    cal = Calendar()
    print("%12s | %12s | %12s " %
          ("day", "volume", "dollars"))

    for day in cal.itermonthdates(year, month):
        if day.month != month:
            continue
        if day in data:
            volume, dollars = data[day]
        else:
            volume, dollars = 0, 0

        print("%12s | %12s | %12s " %
              (day, volume, dollars))


if __name__ == '__main__':
    # year = int(sys.argv[1])
    # month = int(sys.argv[2])

    list_for_month(2010, 12)
