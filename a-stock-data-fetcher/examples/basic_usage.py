"""
A股数据获取示例脚本
演示如何使用各个模块获取股票数据
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stock_history import StockHistoryFetcher
from stock_financial import StockFinancialFetcher
from stock_info import StockInfoFetcher


def example_get_history_data():
    """示例：获取历史交易数据"""
    print("\n" + "="*60)
    print("示例1: 获取股票历史交易数据")
    print("="*60)

    # 创建历史数据获取器
    fetcher = StockHistoryFetcher()

    # 获取浦发银行(600000)的日K线数据
    stock_code = "600000"
    print(f"\n获取 {stock_code} 的日K线数据...")

    df = fetcher.get_daily_kline(
        symbol=stock_code,
        start_date="20230101",
        end_date="20231231",
        adjust="qfq"  # 前复权
    )

    if not df.empty:
        print("\n前5条数据:")
        print(df.head())

        # 保存到文件
        output_file = f"../data/{stock_code}_daily.csv"
        fetcher.save_to_csv(df, output_file)


def example_get_financial_data():
    """示例：获取财务指标数据"""
    print("\n" + "="*60)
    print("示例2: 获取股票财务指标数据")
    print("="*60)

    # 创建财务数据获取器
    fetcher = StockFinancialFetcher()

    # 获取贵州茅台(600519)的财务指标
    stock_code = "600519"
    print(f"\n获取 {stock_code} 的财务指标...")

    df = fetcher.get_financial_indicators(symbol=stock_code)

    if not df.empty:
        print("\n财务指标数据:")
        print(df.head())

        # 保存到文件
        output_file = f"../data/{stock_code}_financial.xlsx"
        fetcher.save_to_excel(df, output_file)

    # 获取PE/PB数据
    print(f"\n获取 {stock_code} 的PE/PB数据...")
    pe_pb_df = fetcher.get_pe_pb_data(symbol=stock_code)

    if not pe_pb_df.empty:
        print("\nPE/PB数据:")
        print(pe_pb_df.head())


def example_get_stock_info():
    """示例：获取股票基本信息"""
    print("\n" + "="*60)
    print("示例3: 获取股票基本信息")
    print("="*60)

    # 创建信息获取器
    fetcher = StockInfoFetcher()

    # 搜索包含"银行"的股票
    keyword = "银行"
    print(f"\n搜索包含'{keyword}'的股票...")

    df = fetcher.search_stock_by_name(keyword)

    if not df.empty:
        print(f"\n找到 {len(df)} 只相关股票:")
        print(df[['代码', '名称', '最新价', '涨跌幅']].head(10))

    # 获取银行行业的所有股票
    industry = "银行"
    print(f"\n获取{industry}行业的所有股票...")

    industry_df = fetcher.get_stocks_by_industry(industry)

    if not industry_df.empty:
        print(f"\n{industry}行业股票:")
        print(industry_df[['代码', '名称', '最新价', '涨跌幅']].head())

        # 保存到文件
        output_file = f"../data/{industry}_stocks.csv"
        fetcher.save_to_csv(industry_df, output_file)

    # 获取上海地区的所有股票
    region = "上海"
    print(f"\n获取{region}地区的所有股票...")

    region_df = fetcher.get_stocks_by_region(region)

    if not region_df.empty:
        print(f"\n{region}地区股票:")
        print(region_df[['代码', '名称', '最新价', '涨跌幅']].head())

        # 保存到文件
        output_file = f"../data/{region}_stocks.csv"
        fetcher.save_to_csv(region_df, output_file)


def example_get_all_stocks():
    """示例：获取所有A股列表"""
    print("\n" + "="*60)
    print("示例4: 获取所有A股股票列表")
    print("="*60)

    fetcher = StockInfoFetcher()

    print("\n正在获取所有A股股票列表...")
    df = fetcher.get_all_stock_list()

    if not df.empty:
        print(f"\nA股市场共有 {len(df)} 只股票")
        print("\n前10只股票:")
        print(df[['代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额']].head(10))

        # 保存到文件
        output_file = "../data/all_a_stocks.csv"
        fetcher.save_to_csv(df, output_file)


def main():
    """主函数"""
    print("A股市场数据获取工具 - 使用示例")
    print("=" * 60)

    # 确保data目录存在
    os.makedirs("../data", exist_ok=True)

    # 运行各个示例
    try:
        example_get_history_data()
    except Exception as e:
        print(f"\n示例1执行出错: {e}")

    try:
        example_get_financial_data()
    except Exception as e:
        print(f"\n示例2执行出错: {e}")

    try:
        example_get_stock_info()
    except Exception as e:
        print(f"\n示例3执行出错: {e}")

    try:
        example_get_all_stocks()
    except Exception as e:
        print(f"\n示例4执行出错: {e}")

    print("\n" + "="*60)
    print("所有示例执行完成！")
    print("数据文件已保存到 data 目录")
    print("="*60)


if __name__ == "__main__":
    main()
