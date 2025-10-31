# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python-based tool for fetching A-share (Chinese stock market) data using the akshare library. The tool provides three main functional modules for retrieving historical trading data, financial indicators, and company information.

## Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Examples
```bash
cd examples
python basic_usage.py
```

The example script demonstrates all three modules and saves output to the `data/` directory.

### Run From Any Location
When importing modules from `src/`, add the parent directory to the Python path:
```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
```

## Architecture

### Module Structure

The codebase is organized into three independent fetcher classes:

1. **StockHistoryFetcher** (`src/stock_history.py`)
   - Fetches K-line data (daily, weekly, monthly)
   - Handles price adjustment types: `qfq` (forward), `hfq` (backward), or no adjustment
   - Uses `ak.stock_zh_a_hist()` with period parameter

2. **StockFinancialFetcher** (`src/stock_financial.py`)
   - Fetches financial statements (balance sheet, income statement, cash flow)
   - Retrieves financial indicators and ratios (ROE, PE/PB)
   - Uses multiple akshare functions: `stock_financial_abstract`, `stock_balance_sheet_by_report_em`, `stock_profit_sheet_by_report_em`, `stock_cash_flow_sheet_by_report_em`, `stock_a_lg_indicator`

3. **StockInfoFetcher** (`src/stock_info.py`)
   - Fetches stock lists and company information
   - Retrieves stocks by industry or concept sector
   - Uses `stock_zh_a_spot_em()` for all stocks, `stock_board_industry_cons_em()` and `stock_board_concept_cons_em()` for sector-specific queries

### Common Patterns

All three fetcher classes follow the same pattern:
- Simple initialization with no parameters
- Methods return pandas DataFrames
- Empty DataFrames returned on errors (exceptions caught internally)
- Print statements for success/error feedback
- Shared `save_to_csv()` and `save_to_excel()` methods with UTF-8 BOM encoding for Chinese characters

### Data Flow

1. User creates a fetcher instance
2. Calls data retrieval method (returns DataFrame)
3. Optionally saves to CSV/Excel using fetcher's save methods
4. Data directory: `data/` (created automatically by examples)

### Stock Code Format

Chinese A-share codes are 6-digit strings:
- Shanghai Stock Exchange: 600xxx, 601xxx, 603xxx, 688xxx
- Shenzhen Stock Exchange: 000xxx, 001xxx, 002xxx, 003xxx, 300xxx

Always pass as strings (e.g., `"600000"`), not integers.

### Date Format

All date parameters use `YYYYMMDD` format as strings (e.g., `"20230101"`).

### Configuration

`config/settings.py` contains default values for:
- Favorite stock codes
- Default date ranges
- Default adjustment type
- Favorite industries and concepts

These are reference constants, not actively used by the fetcher classes.

### Dependencies

The project relies heavily on akshare for data retrieval. All akshare API calls are wrapped in try-except blocks to handle network errors or API changes gracefully.
