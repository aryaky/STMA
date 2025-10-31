"""
配置文件
"""

# 数据源配置
DATA_SOURCE = "akshare"

# 超时设置（秒）
REQUEST_TIMEOUT = 10

# 重试次数
MAX_RETRIES = 3

# 市场代码映射
MARKET_MAP = {
    "sh": "上海",
    "sz": "深圳",
    "bj": "北京"
}
