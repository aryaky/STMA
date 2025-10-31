"""
获取A股财务指标数据模块
使用akshare库获取股票的财务报表、财务指标等数据
"""

import akshare as ak
import pandas as pd
from typing import Optional, Literal


class StockFinancialFetcher:
    """股票财务数据获取器"""

    def __init__(self):
        """初始化财务数据获取器"""
        pass

    def get_financial_indicators(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的主要财务指标

        参数:
            symbol: 股票代码，如'600000'

        返回:
            DataFrame包含每股收益、净资产收益率、市盈率等财务指标
        """
        try:
            # 获取财务指标数据
            df = ak.stock_financial_abstract(symbol=symbol)

            print(f"成功获取股票 {symbol} 的财务指标，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 财务指标时出错: {e}")
            return pd.DataFrame()

    def get_balance_sheet(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的资产负债表

        参数:
            symbol: 股票代码

        返回:
            DataFrame包含资产负债表数据
        """
        try:
            # 获取资产负债表
            df = ak.stock_balance_sheet_by_report_em(symbol=symbol)

            print(f"成功获取股票 {symbol} 的资产负债表，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 资产负债表时出错: {e}")
            return pd.DataFrame()

    def get_income_statement(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的利润表

        参数:
            symbol: 股票代码

        返回:
            DataFrame包含利润表数据
        """
        try:
            # 获取利润表
            df = ak.stock_profit_sheet_by_report_em(symbol=symbol)

            print(f"成功获取股票 {symbol} 的利润表，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 利润表时出错: {e}")
            return pd.DataFrame()

    def get_cash_flow(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的现金流量表

        参数:
            symbol: 股票代码

        返回:
            DataFrame包含现金流量表数据
        """
        try:
            # 获取现金流量表
            df = ak.stock_cash_flow_sheet_by_report_em(symbol=symbol)

            print(f"成功获取股票 {symbol} 的现金流量表，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 现金流量表时出错: {e}")
            return pd.DataFrame()

    def get_roe_data(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的净资产收益率(ROE)数据

        参数:
            symbol: 股票代码

        返回:
            DataFrame包含ROE历史数据
        """
        try:
            # 获取股票的财务指标
            df = ak.stock_financial_abstract(symbol=symbol)

            # 筛选ROE相关数据
            if '净资产收益率' in df.columns:
                roe_df = df[['报告期', '净资产收益率']]
                print(f"成功获取股票 {symbol} 的ROE数据，共 {len(roe_df)} 条记录")
                return roe_df
            else:
                print(f"未找到股票 {symbol} 的ROE数据")
                return df

        except Exception as e:
            print(f"获取股票 {symbol} ROE数据时出错: {e}")
            return pd.DataFrame()

    def get_pe_pb_data(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的市盈率(PE)和市净率(PB)数据

        参数:
            symbol: 股票代码

        返回:
            DataFrame包含PE和PB数据
        """
        try:
            # 获取个股的历史市盈率和市净率
            df = ak.stock_a_lg_indicator(symbol=symbol)

            if not df.empty:
                print(f"成功获取股票 {symbol} 的PE/PB数据，共 {len(df)} 条记录")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} PE/PB数据时出错: {e}")
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
