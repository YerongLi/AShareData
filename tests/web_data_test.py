import datetime as dt
import unittest

from AShareData.DateUtils import TradingCalendar
from AShareData.DBInterface import MySQLInterface, prepare_engine
from AShareData.WebData import WebDataCrawler


class WebDataSourceTest(unittest.TestCase):
    def setUp(self) -> None:
        config_loc = 'config.json'
        engine = prepare_engine(config_loc)
        db_interface = MySQLInterface(engine)
        self.web_crawler = WebDataCrawler(db_interface)
        self.calendar = TradingCalendar(db_interface)

    def test_sw_industry(self):
        self.web_crawler.get_sw_industry()

    def test_zx_industry(self):
        self.web_crawler.get_zz_industry(self.calendar.offset(dt.date.today(), -1))


if __name__ == '__main__':
    unittest.main()
