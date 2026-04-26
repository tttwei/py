import streamlit as st
from decimal import Decimal, ROUND_HALF_UP
import akshare as ak
from datetime import datetime

st.title("ETF 实时增长率分析")

def query_nbBK(now):
    output = ""
    max_rate = -999
    max_name = '无'
    etf_list = ['512880', '512800', '167301', '159611', '159934', '159941', '159920']
    for name in etf_list:
        df = ak.fund_etf_hist_em(symbol=f"{name}", period="daily", start_date="20250401", end_date=f"{now}", adjust="qfq")
        old_price = df.iloc[-8,2]
        new_price = df.iloc[-1,2]
        new_growth_rate = (Decimal(str(new_price))-Decimal(str(old_price)))/Decimal(str(old_price))
        n1 = (new_growth_rate*100).quantize(Decimal('0.00000'), rounding=ROUND_HALF_UP)
        output += f'{name} 增长率: {n1}%\n'
        if new_growth_rate > max_rate:
            max_rate = new_growth_rate
            max_name = name

    date = df.iloc[-1, 0]
    date2 = df.iloc[-8, 0]
    output += f"\n当前检索时间：{date}\n7天前时间：{date2}\n"

    if max_rate < 0:
        output += "建议：空仓\n"
    else:
        output += f"建议：买入 {max_name}\n"

    return output

if st.button("运行分析"):
    now_date = datetime.today().strftime('%Y%m%d')
    result = query_nbBK(now_date)
    st.text(result)
