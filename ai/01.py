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
        print(f"请求失败：{code} 状态码 {r.status_code}")
        return pd.DataFrame()

    try:
        data = r.json()
    except Exception as e:
        print(f"解析 JSON 失败：{code} 错误：{e}")
        return pd.DataFrame()

    if not data or not data.get("data") or not data["data"].get("klines"):
        print(f"数据为空或格式错误：{code}")
        return pd.DataFrame()

    kline = data["data"]["klines"]
    df = pd.DataFrame([line.split(",") for line in kline], columns=[
        "date", "open", "close", "high", "low", "volume", "amount", "_", "_", "_", "_"
    ])
    df["close"] = pd.to_numeric(df["close"], errors='coerce')
    return df

# 获取当前日期
current_date = datetime.today()
now_date = current_date.strftime('%Y%m%d')
print("现在时间：", now_date)

def query_nbBK(now):
    max_rate = Decimal('-999')
    max_name = '无'

    etf_list = ['512880', '512800', '167301', '159611', '159934', '159941', '159920']
    for name in etf_list:
        df = get_etf_data(name, "20250601", now)
        if df.empty or len(df) < 8:
            print(f"{name} 数据不足")
            continue

        old_price = df.iloc[-8]["close"]
        new_price = df.iloc[-1]["close"]

        if pd.isna(old_price) or pd.isna(new_price):
            print(f"{name} 收盘价缺失")
            continue

        new_growth_rate = (Decimal(str(new_price)) - Decimal(str(old_price))) / Decimal(str(old_price))
        n1 = (new_growth_rate * 100).quantize(Decimal('0.00000'), rounding=ROUND_HALF_UP)
        print(f'{name} 增长率 {n1}%')

        if new_growth_rate > max_rate:
            max_rate = new_growth_rate
            max_name = name

        date = df.iloc[-1]["date"]
        date2 = df.iloc[-8]["date"]
    print("当前检索使用时间：", date)
    print("7天前时间：", date2)

    if max_rate < 0:
        print("空仓")
    else:
        print("买：", max_name)

query_nbBK(now_date)
