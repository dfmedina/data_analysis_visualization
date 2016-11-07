import psycopg2

conn = psycopg2.connect("host='localhost' port='5432' dbname='dav' user='dba' password='root'")
print "Connection open"
cur = conn.cursor()
f = open(r'C:\Globant\mentoring\WIKI_PRICES.csv', 'r')

try:
    print "importing data"  # TODO: add this to log
    cur.execute('TRUNCATE dav.data_landing;')
    cur.copy_from(f,
                  'dav.data_landing',
                  columns=('ticker', 'date', 'open', 'high', 'low', 'close', 'volume', '"ex-dividend"',
                           'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume'),
                  sep=',')
except Exception, e:
    print e.message
    # print "Data could not be imported"  # TODO: add this to log

f.close()
conn.close()
