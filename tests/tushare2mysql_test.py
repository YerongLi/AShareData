import json
import unittest

from AShareData.DBInterface import MySQLInterface, prepare_engine
from AShareData.TushareData import TushareData


class Tushare2MySQLTest(unittest.TestCase):
    def setUp(self) -> None:
        config_loc = 'config.json'
        with open(config_loc, 'r') as f:
            config = json.load(f)

        tushare_token = config['tushare_token']
        self.downloader = TushareData(tushare_token, MySQLInterface(prepare_engine(config_loc), init=False))

    def test_calendar(self):
        print(self.downloader.calendar.calendar)

    def test_financial(self):
        self.downloader.get_financial(['300146.SZ', '000001.SZ'])

    def test_index(self):
        self.downloader.get_index_daily()

    def test_ipo_info(self):
        self.downloader.get_ipo_info()

    def test_all_past_names(self):
        self.downloader.init_stock_names()

    def test_past_names(self):
        self.downloader.update_stock_names()

    def test_company_info(self):
        self.downloader.get_company_info()

    def test_daily_hq(self):
        self.downloader.get_daily_hq(start_date='2010917')

    def test_all_dividend(self):
        self.downloader.get_all_dividend()

    def test_routine(self):
        # self.downloader.update_routine()
        pass

    def test_hs_const(self):
        self.downloader.get_hs_constitute()

    def test_shibor(self):
        self.downloader.get_shibor(end_date='20111010')

    def test_index_weight(self):
        self.downloader.get_index_weight(start_date='20050101')


if __name__ == '__main__':
    unittest.main()
