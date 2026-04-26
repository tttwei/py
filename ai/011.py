import streamlit as st
from decimal import Decimal, ROUND_HALF_UP
import pandas as pd
import requests
from datetime import datetime

etf_list = {
    '512880': '1',  # 沪
    '512800': '1',
    '167301': '0',
    '159611': '0',  # 深
    '159934': '0',
    '159941': '0',
    '159920': '0',
}

def get_etf_data(code, start_date, end_date):
    url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
    params = {
        "secid": f"{etf_list[code]}.{code}",
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": "101",
        "fqt": "1",
        "beg": start_date,
        "end": end_date
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        return pd.DataFrame()

    try:
        data = r.json()
    except Exception:
        return pd.DataFrame()

    if not data or not data.get("data") or not data["data"].get("klines"):
        return pd.DataFrame()

    kline = data["data"]["klines"]
    df = pd.DataFrame([line.split(",") for line in kline], columns=[
        "date", "open", "close", "high", "low", "volume", "amount", "_", "_", "_", "_"
    ])
    df["close"] = pd.to_numeric(df["close"], errors='coerce')
    return df

def query_nbBK(now):
    output = []
    max_rate = Decimal('-999')
    max_name = '无'

    for name in etf_list:
        df = get_etf_data(name, "20250601", now)
        if df.empty or len(df) < 8:
            output.append(f"{name} 数据不足")
            continue

        old_price = df.iloc[-8]["close"]
        new_price = df.iloc[-1]["close"]

        if pd.isna(old_price) or pd.isna(new_price):
            output.append(f"{name} 收盘价缺失")
            continue

        new_growth_rate = (Decimal(str(new_price)) - Decimal(str(old_price))) / Decimal(str(old_price))
        n1 = (new_growth_rate * 100).quantize(Decimal('0.00000'), rounding=ROUND_HALF_UP)
        output.append(f'{name} 增长率 {n1}%')

        if new_growth_rate > max_rate:
            max_rate = new_growth_rate
            max_name = name

        date = df.iloc[-1]["date"]
        date2 = df.iloc[-8]["date"]

    if max_rate < 0:
        output.append("建议：空仓")
    else:
        output.append(f"建议：买入 {max_name}")
    output.append(f"当前检索使用时间：{date}")
    output.append(f"7天前时间：{date2}")

    return output

# Streamlit 页面
st.title("ETF 策略建议查询")

if st.button("点击获取建议"):
    now_date = datetime.today().strftime('%Y%m%d')
    result = query_nbBK(now_date)
    for line in result:
        st.write(line)
