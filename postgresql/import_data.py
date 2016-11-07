import psycopg2

conn = psycopg2.connect("host='localhost' port='5432' dbname='dav' user='dba' password='root'")
cur = conn.cursor()
f = open(r'C:\Globant\mentoring\WIKI_PRICES.csv', 'r')
cur.copy_from(f,
              'dav.data_landing',
              columns=('ticker', 'date', 'open', 'high', 'low', 'close', 'volume', '"ex-dividend"',
                       'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume'),
              sep=',')
f.close()
