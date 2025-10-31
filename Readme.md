# STMA - 股票市场分析工具集

本仓库包含两个用于中国A股市场数据获取和分析的Python项目。

## 📊 项目概览

### 1. a-stock-data-fetcher - 完整的A股数据获取工具

**状态**: ✅ 生产就绪，功能完善

一个功能完备的Python工具，用于获取中国A股市场的各类数据，包括历史交易数据、财务指标和公司基本信息。

**核心功能**:
- 📈 历史交易数据（K线数据）- 日线/周线/月线，支持前复权/后复权
- 💰 财务报表 - 资产负债表、利润表、现金流量表
- 📊 财务指标 - ROE（净资产收益率）、PE（市盈率）、PB（市净率）
- 🏢 公司信息 - 基本信息、股东信息、行业分类、概念板块、地域分类

**技术栈**:
- Python 3.x
- akshare >= 1.12.0 (数据源)
- pandas >= 2.0.0 (数据处理)
- numpy >= 1.24.0 (数值计算)
- openpyxl >= 3.1.0 (Excel导出)
- requests >= 2.31.0 (HTTP请求)

**目录结构**:
```
a-stock-data-fetcher/
├── README.md           # 完整的中文文档
├── CLAUDE.md          # 开发者指南
├── config/
│   └── settings.py    # 配置文件（常用股票、行业、概念等）
├── data/              # 数据存储目录
├── examples/
│   └── basic_usage.py # 完整的使用示例
├── requirements.txt   # Python依赖
└── src/               # 源代码模块
    ├── stock_history.py    # 历史交易数据
    ├── stock_financial.py  # 财务数据
    └── stock_info.py       # 公司信息
```

**快速开始**:
```bash
cd a-stock-data-fetcher
pip install -r requirements.txt
python examples/basic_usage.py
```

详细文档请查看: [a-stock-data-fetcher/README.md](a-stock-data-fetcher/README.md)

---

### 2. xstock - 精简的股票信息系统

**状态**: 🚧 早期开发阶段

一个更加精简的股票信息检索系统，专注于A股基本信息查询。目前处于早期开发阶段，仅实现了基础功能。

**已实现功能**:
- 📋 获取个股基本信息
- 📊 获取全部A股列表
- 🔍 按关键字搜索股票（代码或名称）

**技术栈**:
- Python 3.x
- akshare >= 1.12.0
- pandas >= 2.0.0
- requests >= 2.31.0

**目录结构**:
```
xstock/
├── requirements.txt
├── src/
│   └── xstock/
│       ├── config.py       # 配置模块（超时、重试等）
│       └── stock_info.py   # 股票信息模块
└── tests/                  # 测试目录（待完善）
```

**计划中的功能**:
- ⏱️ 实时行情数据 (`RealtimeQuote` 模块)
- 📈 历史数据获取 (`HistoricalData` 模块)
- 📚 完整的文档和示例
- ✅ 单元测试

---

## 🔄 两个项目的对比

| 特性 | a-stock-data-fetcher | xstock |
|------|---------------------|--------|
| **成熟度** | 生产就绪 | 早期开发 |
| **功能完整性** | 全面（历史、财务、信息） | 基础（仅信息查询） |
| **文档** | 完整的中英文文档 | 无文档 |
| **示例代码** | 完整的使用示例 | 无示例 |
| **配置管理** | 基础配置文件 | 更好的配置模块 |
| **依赖项** | 较多（含Excel支持） | 精简 |
| **适用场景** | 全面的股票数据分析 | 轻量级信息查询 |

---

## 🚀 推荐使用

- **如果您需要全面的股票数据分析功能**: 使用 **a-stock-data-fetcher**，它提供了完整的历史数据、财务报表、公司信息等功能，文档齐全，可直接投入生产使用。

- **如果您只需要基本的股票信息查询**: 可以关注 **xstock** 项目的后续开发，它采用更精简的设计，未来可能提供更轻量级的解决方案。

---

## 📝 数据源说明

两个项目均使用 [akshare](https://github.com/akfamily/akshare) 作为数据源。akshare 是一个优秀的开源财经数据接口库，提供免费的中国股票、期货、基金、债券等金融数据。

---

## 📄 许可证

请查看各子项目的许可证说明。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**最后更新**: 2025-10-31
