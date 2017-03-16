import psycopg2
import os
import logging

class DataImporter(object):
    logging.basicConfig(filename='dav.log', level=logging.INFO)

    def __init__(self, dbname, user, passwd='root', host='localhost', port=5432):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        self.port = port


    def import_data(self, schema, table, import_columns, prices_dataset):
        logging.info('Starting connection to database')
        conn = psycopg2.connect("host='%s' port='%d' dbname='%s' user='%s' password='%s'"
                                % (self.host, self.port, self.dbname, self.user, self.passwd))
        logging.info('Connection open')
        cur = conn.cursor()
        logging.info('Opening data-set')
        with open(r'%s' % prices_dataset, 'r') as f:
            try:
                logging.info('Truncate existing data')
                cur.execute('TRUNCATE '+schema+"."+table+';')
                logging.info('Importing data')
                cur.copy_from(f, schema+"."+table, columns=import_columns, sep=',')
                conn.commit()
                logging.info('Data imported')
            except Exception, e:
                logging.error(e.message)
                logging.error('Error importing data')
        conn.close()

if __name__ == '__main__':
        dir_path = os.path.dirname(os.path.abspath(__file__))

        data_landing_col = ('ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'ex_dividend',
                            'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume')

        companies_col = ('symbol', 'name', 'last_sale', 'market_cap', 'country',
                         'ipo_year', 'sector', 'industry')

        prices_dataset = os.path.join(dir_path, '../datasets/WIKI_PRICES.csv')
        companies_dataset = os.path.join(dir_path, '../datasets/companylist.csv')

        importer = DataImporter('dav', 'dba')
        importer.import_data('dav', 'company_landing', companies_col, companies_dataset)
        importer.import_data('dav', 'data_landing', data_landing_col, prices_dataset)

# TODO: create unittest
