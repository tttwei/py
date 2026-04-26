from decimal import Decimal, ROUND_HALF_UP

# import pandas as pd
# print(pd.__version__)
import akshare as ak
# from sqlalchemy import create_engine

from datetime import datetime

# from dateutil.relativedelta import relativedelta

# 获取当前日期
current_date = datetime.today()

# 格式化为 YYYYMMDD 格式
now_date = current_date.strftime('%Y%m%d')


# 获取当前日期
current_date = datetime.today()

# 获取前一个月的日期
# previous_month = current_date - relativedelta(months=1)

print("现在时间：",now_date)

# print(previous_month)

# engine = create_engine('mysql+pymysql://root:123456@localhost:3306/machine_trading')



def query_nbBK(now):
    max_rate = -999
    max_name = '无'

    # 创建示例 DataFrame，假设你已有的数据
    etf_list = ['512880', '512800', '167301', '159611', '159934', '159941', '159920']
    for name in etf_list:
    # data = {'name': ['David', 'Eve'], 'age': [28, 22]}
        df = ak.fund_etf_hist_em(symbol=f"{name}", period="daily", start_date="20250401", end_date=f"{now}", adjust="qfq")
        # print(df.iloc[-8,2])
        old_price = df.iloc[-8,2]
        # print(df.iloc[-1,2])
        new_price = df.iloc[-1,2]

        new_growth_rate = (Decimal(str(new_price))-Decimal(str(old_price)))/Decimal(str(old_price))
        n1 = (new_growth_rate*100).quantize(Decimal('0.00000'), rounding=ROUND_HALF_UP)
        print(f'{name}增长率{n1}')

        if new_growth_rate > max_rate:
            max_rate = new_growth_rate
            max_name = name

    date = df.iloc[-1, 0]
    date2 = df.iloc[-8, 0]
    if max_rate < 0:
        print("空仓")
    else:
        print("买：",max_name)
    print("当前检索使用时间：",date)
    print("7天前时间：",date2)

query_nbBK(now_date)