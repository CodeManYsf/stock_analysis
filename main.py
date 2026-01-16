import pandas as pd
import numpy as np
import os

def calculate_rsi(data, periods=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def analyze_stock_strategy():
    print("🤖 Vibe Coding Agent: 初始化量化分析模块...")
    
    # 模拟数据
    prices = [10.0, 10.2, 10.5, 11.0, 11.5, 12.0, 11.8, 11.2, 10.5, 10.0]
    dates = pd.date_range(start='2026-01-01', periods=len(prices))
    
    df = pd.DataFrame({'Date': dates, 'Close': prices})
    
    # 计算指标
    df['RSI'] = calculate_rsi(df['Close'], periods=6)
    
    # --- 新增功能：保存数据 ---
    filename = 'trading_log.csv'
    df.to_csv(filename, index=False)
    print(f"💾 数据已保存至: {os.path.abspath(filename)}")
    # -----------------------

    current_rsi = df['RSI'].iloc[-1]
    print(f"📊 当前 RSI(6): {current_rsi:.2f}")

if __name__ == "__main__":
    analyze_stock_strategy()