"""
配置文件示例
可以在这里配置常用的股票代码、日期范围等参数
"""

# 常用股票代码
FAVORITE_STOCKS = [
    "600000",  # 浦发银行
    "600519",  # 贵州茅台
    "600036",  # 招商银行
    "000001",  # 平安银行
    "000002",  # 万科A
]

# 默认日期范围
DEFAULT_START_DATE = "20200101"
DEFAULT_END_DATE = "20231231"

# 复权方式
DEFAULT_ADJUST = "qfq"  # qfq:前复权, hfq:后复权, '':不复权

# 数据保存路径
DATA_DIR = "../data"

# 常用行业
FAVORITE_INDUSTRIES = [
    "银行",
    "证券",
    "保险",
    "房地产",
    "医药生物",
]

# 常用概念
FAVORITE_CONCEPTS = [
    "人工智能",
    "新能源汽车",
    "芯片",
    "5G",
    "大数据",
]
