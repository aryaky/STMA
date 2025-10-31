# A股市场数据获取工具

一个基于Python的A股市场数据获取工具，使用akshare库获取股票的历史交易数据、财务指标和公司基本信息。

## 功能特点

- **历史交易数据**：获取日K线、周K线、月K线数据，支持前复权、后复权
- **财务指标**：获取资产负债表、利润表、现金流量表、ROE、PE/PB等财务数据
- **公司信息**：获取股票基本信息、行业分类、概念板块、股东信息等
- **数据导出**：支持将数据导出为CSV和Excel格式

## 项目结构

```
a-stock-data-fetcher/
├── src/                    # 源代码目录
│   ├── __init__.py
│   ├── stock_history.py    # 历史交易数据模块
│   ├── stock_financial.py  # 财务指标数据模块
│   └── stock_info.py       # 公司基本信息模块
├── examples/               # 示例代码目录
│   └── basic_usage.py      # 基本使用示例
├── data/                   # 数据存储目录
├── config/                 # 配置文件目录
└── requirements.txt        # 依赖包列表
```

## 安装依赖

```bash
# 进入项目目录
cd a-stock-data-fetcher

# 安装依赖包
pip install -r requirements.txt
```

## 快速开始

### 1. 获取历史交易数据

```python
from src.stock_history import StockHistoryFetcher

# 创建获取器
fetcher = StockHistoryFetcher()

# 获取浦发银行(600000)的日K线数据
df = fetcher.get_daily_kline(
    symbol="600000",
    start_date="20230101",
    end_date="20231231",
    adjust="qfq"  # 前复权
)

# 保存数据
fetcher.save_to_csv(df, "data/600000_daily.csv")
```

### 2. 获取财务指标数据

```python
from src.stock_financial import StockFinancialFetcher

# 创建获取器
fetcher = StockFinancialFetcher()

# 获取贵州茅台(600519)的财务指标
df = fetcher.get_financial_indicators(symbol="600519")

# 获取PE/PB数据
pe_pb_df = fetcher.get_pe_pb_data(symbol="600519")

# 获取资产负债表
balance_df = fetcher.get_balance_sheet(symbol="600519")

# 保存数据
fetcher.save_to_excel(df, "data/600519_financial.xlsx")
```

### 3. 获取公司基本信息

```python
from src.stock_info import StockInfoFetcher

# 创建获取器
fetcher = StockInfoFetcher()

# 获取所有A股列表
all_stocks = fetcher.get_all_stock_list()

# 搜索股票
bank_stocks = fetcher.search_stock_by_name("银行")

# 获取银行行业的所有股票
industry_stocks = fetcher.get_stocks_by_industry("银行")

# 获取人工智能概念股
concept_stocks = fetcher.get_stocks_by_concept("人工智能")

# 保存数据
fetcher.save_to_csv(all_stocks, "data/all_stocks.csv")
```

## 运行示例

项目提供了完整的使用示例：

```bash
# 进入examples目录
cd examples

# 运行示例脚本
python basic_usage.py
```

示例脚本会：
1. 获取指定股票的历史交易数据
2. 获取股票的财务指标和PE/PB数据
3. 搜索特定关键字的股票
4. 获取行业板块的所有股票
5. 获取所有A股股票列表
6. 将数据保存到data目录

## API文档

### StockHistoryFetcher

历史交易数据获取器

**方法：**
- `get_daily_kline(symbol, start_date, end_date, adjust)` - 获取日K线数据
- `get_weekly_kline(symbol, start_date, end_date, adjust)` - 获取周K线数据
- `get_monthly_kline(symbol, start_date, end_date, adjust)` - 获取月K线数据
- `save_to_csv(df, filename)` - 保存为CSV文件
- `save_to_excel(df, filename)` - 保存为Excel文件

**参数说明：**
- `symbol`: 股票代码，如'600000'
- `start_date`: 开始日期，格式'20230101'
- `end_date`: 结束日期，格式'20231231'
- `adjust`: 复权类型，'qfq'前复权，'hfq'后复权，''不复权

### StockFinancialFetcher

财务指标数据获取器

**方法：**
- `get_financial_indicators(symbol)` - 获取财务指标
- `get_balance_sheet(symbol)` - 获取资产负债表
- `get_income_statement(symbol)` - 获取利润表
- `get_cash_flow(symbol)` - 获取现金流量表
- `get_roe_data(symbol)` - 获取ROE数据
- `get_pe_pb_data(symbol)` - 获取PE/PB数据
- `save_to_csv(df, filename)` - 保存为CSV文件
- `save_to_excel(df, filename)` - 保存为Excel文件

### StockInfoFetcher

公司基本信息获取器

**方法：**
- `get_all_stock_list()` - 获取所有A股列表
- `get_stock_individual_info(symbol)` - 获取个股详细信息
- `get_stock_industry_info()` - 获取行业分类信息
- `get_stocks_by_industry(industry_name)` - 获取指定行业的股票
- `get_stock_concept_info()` - 获取概念板块信息
- `get_stocks_by_concept(concept_name)` - 获取指定概念的股票
- `get_stock_holder_info(symbol)` - 获取股东信息
- `search_stock_by_name(keyword)` - 搜索股票
- `save_to_csv(df, filename)` - 保存为CSV文件
- `save_to_excel(df, filename)` - 保存为Excel文件

## 常见股票代码

- 600000 - 浦发银行
- 600519 - 贵州茅台
- 000001 - 平安银行
- 000002 - 万科A
- 600036 - 招商银行

## 注意事项

1. **数据来源**：本工具使用akshare库获取数据，数据来源于公开市场
2. **使用频率**：请合理使用，避免频繁请求导致IP被封
3. **数据延迟**：部分数据可能存在延迟，仅供参考
4. **投资建议**：本工具仅供学习和研究使用，不构成投资建议

## 依赖包

- akshare >= 1.12.0
- pandas >= 2.0.0
- numpy >= 1.24.0
- openpyxl >= 3.1.0
- requests >= 2.31.0

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎提Issue。

## 更新日志

### v1.0.0 (2025-10-20)
- 初始版本发布
- 支持获取历史交易数据
- 支持获取财务指标数据
- 支持获取公司基本信息
- 提供完整的使用示例
