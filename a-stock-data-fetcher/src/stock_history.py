"""
获取A股历史交易数据模块
使用akshare库获取股票的日K线、周K线、月K线等历史数据
"""

import akshare as ak
import pandas as pd
from typing import Optional, Literal


class StockHistoryFetcher:
    """股票历史交易数据获取器"""

    def __init__(self):
        """初始化历史数据获取器"""
        pass

    def get_daily_kline(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        adjust: Literal["qfq", "hfq", ""] = "qfq"
    ) -> pd.DataFrame:
        """
        获取股票日K线数据

        参数:
            symbol: 股票代码，如'600000'（浦发银行）
            start_date: 开始日期，格式'20200101'
            end_date: 结束日期，格式'20231231'
            adjust: 复权类型，'qfq'前复权，'hfq'后复权，''不复权

        返回:
            DataFrame包含日期、开盘价、收盘价、最高价、最低价、成交量、成交额等
        """
        try:
            # 使用akshare获取股票历史行情数据
            df = ak.stock_zh_a_hist(
                symbol=symbol,
                period="daily",
                start_date=start_date or "20200101",
                end_date=end_date or pd.Timestamp.now().strftime("%Y%m%d"),
                adjust=adjust
            )

            print(f"成功获取股票 {symbol} 的日K线数据，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 日K线数据时出错: {e}")
            return pd.DataFrame()

    def get_weekly_kline(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        adjust: Literal["qfq", "hfq", ""] = "qfq"
    ) -> pd.DataFrame:
        """
        获取股票周K线数据

        参数:
            symbol: 股票代码
            start_date: 开始日期
            end_date: 结束日期
            adjust: 复权类型

        返回:
            DataFrame包含周K线数据
        """
        try:
            df = ak.stock_zh_a_hist(
                symbol=symbol,
                period="weekly",
                start_date=start_date or "20200101",
                end_date=end_date or pd.Timestamp.now().strftime("%Y%m%d"),
                adjust=adjust
            )

            print(f"成功获取股票 {symbol} 的周K线数据，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 周K线数据时出错: {e}")
            return pd.DataFrame()

    def get_monthly_kline(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        adjust: Literal["qfq", "hfq", ""] = "qfq"
    ) -> pd.DataFrame:
        """
        获取股票月K线数据

        参数:
            symbol: 股票代码
            start_date: 开始日期
            end_date: 结束日期
            adjust: 复权类型

        返回:
            DataFrame包含月K线数据
        """
        try:
            df = ak.stock_zh_a_hist(
                symbol=symbol,
                period="monthly",
                start_date=start_date or "20200101",
                end_date=end_date or pd.Timestamp.now().strftime("%Y%m%d"),
                adjust=adjust
            )

            print(f"成功获取股票 {symbol} 的月K线数据，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 月K线数据时出错: {e}")
            return pd.DataFrame()

    def save_to_csv(self, df: pd.DataFrame, filename: str) -> None:
        """
        将数据保存为CSV文件

        参数:
            df: 要保存的DataFrame
            filename: 文件名
        """
        if not df.empty:
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            print(f"数据已保存到 {filename}")
        else:
            print("数据为空，未保存")

    def save_to_excel(self, df: pd.DataFrame, filename: str) -> None:
        """
        将数据保存为Excel文件

        参数:
            df: 要保存的DataFrame
            filename: 文件名
        """
        if not df.empty:
            df.to_excel(filename, index=False, engine='openpyxl')
            print(f"数据已保存到 {filename}")
        else:
            print("数据为空，未保存")
