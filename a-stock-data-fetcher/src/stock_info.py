"""
获取A股公司基本信息模块
使用akshare库获取股票的基本信息、行业分类、上市信息等
"""

import akshare as ak
import pandas as pd
from typing import Optional


class StockInfoFetcher:
    """股票基本信息获取器"""

    def __init__(self):
        """初始化信息获取器"""
        pass

    def get_all_stock_list(self) -> pd.DataFrame:
        """
        获取所有A股股票列表

        返回:
            DataFrame包含股票代码、名称、上市日期等基本信息
        """
        try:
            # 获取沪深京A股实时行情数据（包含基本信息）
            df = ak.stock_zh_a_spot_em()

            print(f"成功获取A股股票列表，共 {len(df)} 只股票")
            return df

        except Exception as e:
            print(f"获取股票列表时出错: {e}")
            return pd.DataFrame()

    def get_stock_individual_info(self, symbol: str) -> pd.DataFrame:
        """
        获取个股的详细信息

        参数:
            symbol: 股票代码，如'600000'

        返回:
            DataFrame包含公司名称、上市日期、总股本、流通股本等详细信息
        """
        try:
            # 获取个股信息
            df = ak.stock_individual_info_em(symbol=symbol)

            print(f"成功获取股票 {symbol} 的详细信息")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 详细信息时出错: {e}")
            return pd.DataFrame()

    def get_stock_industry_info(self) -> pd.DataFrame:
        """
        获取股票的行业分类信息

        返回:
            DataFrame包含股票代码、行业分类等信息
        """
        try:
            # 获取行业板块成份股
            df = ak.stock_board_industry_name_em()

            print(f"成功获取行业分类信息，共 {len(df)} 个行业")
            return df

        except Exception as e:
            print(f"获取行业分类信息时出错: {e}")
            return pd.DataFrame()

    def get_stocks_by_industry(self, industry_name: str) -> pd.DataFrame:
        """
        获取指定行业的所有股票

        参数:
            industry_name: 行业名称，如'银行'

        返回:
            DataFrame包含该行业所有股票的信息
        """
        try:
            # 获取指定行业板块的成份股
            df = ak.stock_board_industry_cons_em(symbol=industry_name)

            print(f"成功获取 {industry_name} 行业的股票，共 {len(df)} 只")
            return df

        except Exception as e:
            print(f"获取 {industry_name} 行业股票时出错: {e}")
            return pd.DataFrame()

    def get_stock_concept_info(self) -> pd.DataFrame:
        """
        获取股票的概念板块信息

        返回:
            DataFrame包含概念板块名称、涨跌幅等信息
        """
        try:
            # 获取概念板块数据
            df = ak.stock_board_concept_name_em()

            print(f"成功获取概念板块信息，共 {len(df)} 个概念")
            return df

        except Exception as e:
            print(f"获取概念板块信息时出错: {e}")
            return pd.DataFrame()

    def get_stocks_by_concept(self, concept_name: str) -> pd.DataFrame:
        """
        获取指定概念板块的所有股票

        参数:
            concept_name: 概念名称，如'人工智能'

        返回:
            DataFrame包含该概念所有股票的信息
        """
        try:
            # 获取指定概念板块的成份股
            df = ak.stock_board_concept_cons_em(symbol=concept_name)

            print(f"成功获取 {concept_name} 概念的股票，共 {len(df)} 只")
            return df

        except Exception as e:
            print(f"获取 {concept_name} 概念股票时出错: {e}")
            return pd.DataFrame()

    def get_stock_region_info(self) -> pd.DataFrame:
        """
        获取股票的地域板块信息

        返回:
            DataFrame包含地域板块名称、涨跌幅等信息
        """
        try:
            # 获取地域板块数据
            df = ak.stock_board_district_name_em()

            print(f"成功获取地域板块信息，共 {len(df)} 个地区")
            return df

        except Exception as e:
            print(f"获取地域板块信息时出错: {e}")
            return pd.DataFrame()

    def get_stocks_by_region(self, region_name: str) -> pd.DataFrame:
        """
        获取指定地域板块的所有股票

        参数:
            region_name: 地域名称，如'北京'、'上海'

        返回:
            DataFrame包含该地区所有股票的信息
        """
        try:
            # 获取指定地域板块的成份股
            df = ak.stock_board_district_cons_em(symbol=region_name)

            print(f"成功获取 {region_name} 地区的股票，共 {len(df)} 只")
            return df

        except Exception as e:
            print(f"获取 {region_name} 地区股票时出错: {e}")
            return pd.DataFrame()

    def get_stock_holder_info(self, symbol: str) -> pd.DataFrame:
        """
        获取股票的股东信息

        参数:
            symbol: 股票代码

        返回:
            DataFrame包含主要股东持股信息
        """
        try:
            # 获取股东信息
            df = ak.stock_gdfx_top_10_em(symbol=symbol)

            print(f"成功获取股票 {symbol} 的股东信息")
            return df

        except Exception as e:
            print(f"获取股票 {symbol} 股东信息时出错: {e}")
            return pd.DataFrame()

    def search_stock_by_name(self, keyword: str) -> pd.DataFrame:
        """
        根据关键字搜索股票

        参数:
            keyword: 搜索关键字，如'银行'、'科技'等

        返回:
            DataFrame包含匹配的股票信息
        """
        try:
            # 先获取所有股票列表
            all_stocks = self.get_all_stock_list()

            if not all_stocks.empty and '名称' in all_stocks.columns:
                # 根据名称筛选
                matched = all_stocks[all_stocks['名称'].str.contains(keyword, na=False)]
                print(f"找到 {len(matched)} 只包含 '{keyword}' 的股票")
                return matched
            else:
                print("无法搜索股票")
                return pd.DataFrame()

        except Exception as e:
            print(f"搜索股票时出错: {e}")
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
