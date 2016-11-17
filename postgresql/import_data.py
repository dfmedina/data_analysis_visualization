import psycopg2
import os
import logging


class DataImporter(object):
    logging.basicConfig(filename='dav.log', level=logging.INFO)

    def __init__(self, dbname, user, passwd='root', host='localhost', port=5432):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        self.dataset = os.path.join(dir_path, '../data/WIKI_PRICES.csv')
        self.host = host
        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        self.port = port

    def import_data(self):
        logging.info('Starting connection to database')
        conn = psycopg2.connect("host='%s' port='%d' dbname='%s' user='%s' password='%s'"
                                % (self.host, self.port, self.dbname, self.user, self.passwd))
        logging.info('Connection open')
        cur = conn.cursor()
        logging.info('Opening dataset')
        with open(r'%s' % self.dataset, 'r') as f:
            try:
                logging.info('Truncate existing data')
                cur.execute('TRUNCATE dav.data_landing;')  # TODO: unittest
                logging.info('Importing data')
                cur.copy_from(f,
                              'dav.data_landing',
                              columns=('ticker', 'date', 'open', 'high', 'low', 'close', 'volume', '"ex-dividend"',
                                       'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume'),
                              sep=',')
                logging.info('Data imported')
            except Exception, e:
                logging.info(e.message)
                logging.info('Error importing data')
        conn.close()

if __name__ == '__main__':
        importer = DataImporter('dav', 'dba')
        importer.import_data()

# TODO: create class with methods, unittest, main application, log
