import pandas as pd
import numpy as np

def calculate_rsi(data, periods=14):
    """
    AI 生成核心算法: 计算 RSI 相对强弱指标
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def analyze_stock_strategy():
    print("🤖 Vibe Coding Agent: 初始化量化分析模块...")
    
    # 模拟一组股票数据 (Close Price)
    prices = [10.0, 10.2, 10.5, 11.0, 11.5, 12.0, 11.8, 11.2, 10.5, 10.0]
    df = pd.DataFrame(prices, columns=['close'])
    
    # 调用算法
    df['rsi'] = calculate_rsi(df['close'], periods=6)
    
    # 输出最后时刻的信号
    current_rsi = df['rsi'].iloc[-1]
    print(f"📊 当前 RSI(6) 指标: {current_rsi:.2f}")
    
    if current_rsi > 80:
        print("🚨 警告: 超买信号触发! (RSI > 80) -> 建议减仓")
    elif current_rsi < 20:
        print("💎 机会: 超卖信号触发! (RSI < 20) -> 建议底仓吸筹")
    else:
        print("⚖️ 状态: 震荡观望中...")

if __name__ == "__main__":
    analyze_stock_strategy()