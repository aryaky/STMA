"""
XStock - 股票信息获取系统
支持获取A股的详情和交易信息
"""

from .stock_info import StockInfo
from .realtime_quote import RealtimeQuote
from .historical_data import HistoricalData

__version__ = "0.1.0"
__all__ = ["StockInfo", "RealtimeQuote", "HistoricalData"]
