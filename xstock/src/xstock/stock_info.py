"""
股票基本信息获取模块
"""

import akshare as ak
import pandas as pd
from typing import Optional, Dict
from .config import REQUEST_TIMEOUT, MAX_RETRIES


class StockInfo:
    """股票基本信息类"""

    def __init__(self):
        """初始化"""
        self.timeout = REQUEST_TIMEOUT
        self.max_retries = MAX_RETRIES

    def get_stock_info(self, symbol: str) -> Optional[Dict]:
        """
        获取股票基本信息

        Args:
            symbol: 股票代码，例如 '000001' 或 '600000'

        Returns:
            股票基本信息字典，包含：
            - code: 股票代码
            - name: 股票名称
            - market: 市场
            - listing_date: 上市日期
            等信息
        """
        try:
            # 获取股票信息
            stock_info_df = ak.stock_individual_info_em(symbol=symbol)

            if stock_info_df is None or stock_info_df.empty:
                return None

            # 将DataFrame转换为字典
            info_dict = {}
            for _, row in stock_info_df.iterrows():
                key = row['item']
                value = row['value']
                info_dict[key] = value

            return info_dict

        except Exception as e:
            print(f"获取股票 {symbol} 信息失败: {str(e)}")
            return None

    def get_all_stocks(self, market: str = "A股") -> Optional[pd.DataFrame]:
        """
        获取所有股票列表

        Args:
            market: 市场类型，可选 "A股"、"港股"、"美股"

        Returns:
            包含所有股票信息的DataFrame
        """
        try:
            if market == "A股":
                # 获取沪深A股实时行情数据
                df = ak.stock_zh_a_spot_em()
                return df
            else:
                print(f"暂不支持 {market} 市场")
                return None

        except Exception as e:
            print(f"获取股票列表失败: {str(e)}")
            return None

    def search_stock(self, keyword: str) -> Optional[pd.DataFrame]:
        """
        搜索股票

        Args:
            keyword: 搜索关键词（股票代码或名称）

        Returns:
            匹配的股票列表
        """
        try:
            all_stocks = self.get_all_stocks()
            if all_stocks is None:
                return None

            # 按代码或名称搜索
            result = all_stocks[
                all_stocks['代码'].str.contains(keyword) |
                all_stocks['名称'].str.contains(keyword)
            ]

            return result

        except Exception as e:
            print(f"搜索股票失败: {str(e)}")
            return None
