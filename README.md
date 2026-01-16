# 📈 A-Share AI Quant Agent (Stock Analysis)

基于 Python 和 Pandas 的 A 股量化分析工具。
集成 RSI 策略算法，自动化监控 A 股趋势，并生成交易日志。

## 🚀 功能特性 (Features)

* **RSI 智能分析**: 自动计算 RSI(6) 指标，识别超买/超卖信号。
* **趋势监控**: 针对 000630 (铜陵有色) 等标的进行盘口分析。
* **数据持久化**: 自动将分析结果导出为 `trading_log.csv`。
* **企业级规范**: 包含 `.gitignore` 配置，防止敏感数据上传。

## 🛠️ 快速开始 (Quick Start)

1.  **安装依赖**:
    ```bash
    pip install pandas numpy
    ```

2.  **运行策略**:
    ```bash
    python main.py
    ```

3.  **查看结果**:
    运行后会在 `data/` 目录生成日志文件。

## 📝 待办清单 (Todo)
- [ ] 接入 Tushare 实时 API 获取真实行情
- [ ] 增加 MACD 指标分析
- [ ] 接入邮件通知功能

---
*Created by CodeManYsf & Vibe Coding Team*