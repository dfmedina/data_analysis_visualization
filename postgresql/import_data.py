import psycopg2
import os

dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(dir, '../data/WIKI_PRICES.csv')

conn = psycopg2.connect("host='localhost' port='5432' dbname='dav' user='dba' password='root'")

print "Connection open"  # TODO: add this to log
cur = conn.cursor()
with open(r'' + dataset + '', 'r') as f:
    try:
        print "importing data"  # TODO: add this to log
        cur.execute('TRUNCATE dav.data_landing;')
        cur.copy_from(f,
                      'dav.data_landing',
                      columns=('ticker', 'date', 'open', 'high', 'low', 'close', 'volume', '"ex-dividend"',
                               'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume'),
                      sep=',')
        print "data imported"  # TODO: add this to log
    except Exception, e:
            print e.message
            # print "Data could not be imported"  # TODO: add this to log
conn.close()


# TODO: create methods, unittest, main application, log,
