import numpy as np
import pandas as pd
from cached_property import cached_property

from . import DateUtils
from .DBInterface import DBInterface
from .Factor import CompactFactor, ContinuousFactor, OnTheRecordFactor
from .Tickers import StockTickers


class AShareDataReader(object):
    """ AShare Data Reader"""

    def __init__(self, db_interface: DBInterface) -> None:
        """
        AShare Data Reader

        :param db_interface: DBInterface
        """
        self.db_interface = db_interface

    @cached_property
    def calendar(self) -> DateUtils.TradingCalendar:
        """交易日历"""
        return DateUtils.TradingCalendar(self.db_interface)

    @cached_property
    def stocks(self) -> StockTickers:
        """股票列表"""
        return StockTickers(self.db_interface)

    @cached_property
    def sec_name(self) -> CompactFactor:
        """股票名称"""
        return CompactFactor(self.db_interface, '证券名称')

    @cached_property
    def adj_factor(self) -> CompactFactor:
        """复权因子"""
        return CompactFactor(self.db_interface, '复权因子')

    @cached_property
    def free_a_shares(self) -> CompactFactor:
        """A股流通股本"""
        return CompactFactor(self.db_interface, 'A股流通股本')

    @cached_property
    def const_limit(self) -> OnTheRecordFactor:
        """一字涨跌停"""
        return OnTheRecordFactor(self.db_interface, '一字涨跌停')

    @cached_property
    def close(self) -> ContinuousFactor:
        """收盘价"""
        return ContinuousFactor(self.db_interface, '股票日行情', '收盘价')

    @cached_property
    def total_share(self) -> CompactFactor:
        """总股本"""
        return CompactFactor(self.db_interface, '总股本')

    def floating_share(self) -> CompactFactor:
        """流通股本"""
        return CompactFactor(self.db_interface, '流通股本')

    # @cached_property
    def market_cap(self):
        """市值"""
        pass

    def log_cap(self):
        pass

    def cap_weight(self):
        pass

    def cap_wighted_return(self):
        pass

    def hfq_close(self):
        pass

    def qfq_close(self):
        pass

    def daily_return(self):
        pass

    def log_return(self):
        pass

    def index_close(self, ts_code: str):
        pass

    def index_return(self, ts_code: str):
        pass

    def shibor_rate(self, maturity: str = '1年'):
        pass
        # return self._db_reader.get_factor('Shibor利率数据', maturity).div(constants.TRADING_DAYS_IN_YEAR)

    def log_shibor_return(self, maturity: str = '1年'):
        pass

    def excess_market_return(self, index_name: str = '沪深300'):
        pass

    def excess_return(self):
        pass

    @DateUtils.dtlize_input_dates
    def index_constitute(self, index: str, date: DateUtils) -> pd.Series:
        return self.db_interface.read_table('指数成分股权重', index_code=index, dates=[date])

    @staticmethod
    def exponential_weight(n: int, half_life: int):
        series = range(-(n - 1), 1)
        return np.exp(np.log(2) * series / half_life)
