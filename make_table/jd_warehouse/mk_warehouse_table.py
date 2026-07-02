import json
import time
from datetime import datetime, timedelta
import pandas as pd

import requests
from application import request_header

my_json = request_header.jd_warehouse_header

my_url='https://szgateway.jd.com/api/inventoryajax/lowcf/v1/inventoryOverview/overviewDetail.ajax'


today = datetime.now()
# 计算前一天日期
yesterday = today - timedelta(days=1)
# 格式化为字符串
# yesterday_str = "2026-05-29"
yesterday_str = yesterday.strftime("%Y-%m-%d")
print("前一天日期：", yesterday_str)
print("前一天日期：", type(yesterday_str))


row = {
    'id':'0',
    '成都': '0',
    '德州': '0',
    '北京': '0',
    '上海': '0',
    '广州': '0',
    '沈阳': '0',
    '武汉': '0',
    '西安': '0',
    '广州大商超': '0',
    '上海零售': '0',
    '武汉大商超': '0',
    '北京大商超': '0',
    '西安大商超': '0',
    '成都大商超': '0',
    '沈阳大商超': '0'
}

df = pd.DataFrame(row,index=[0,1,2,3,4,5,6,7,8])

df['id'] = ['100339810862',
'100340414948',
'100339810828',
'100339810826',
'100340414968',
'100339810882',
'100369453694',
'100349174078',
'100349174076']

for i in range(len(df['id'])):
    # f = open(f'w{i+1}.json','r',encoding='utf-8')
    # print(f)
    print(f'开始执行，第{i}')
    time.sleep(3)
    my_data = {"startDate": yesterday_str, "endDate": yesterday_str, "compareStartDate": yesterday_str,
               "compareEndDate": yesterday_str,
               "compareType": "yoy", "dateType": "yestoday", "tab": "stockingWarehouseAnalysis",
               "brandCode": ["142649"],
               "thirdCategoryId": ["36956"],
               "kpis": ["spotStockTurnover", "instockPvRatio", "instockRatio", "bsInstockRatio", "stockAmt",
                        "stockQtty", "spotStockAmt",
                        "spotStockQtty", "usableStockAmt", "availableStockQtty", "canOrdQtty", "outWhSaleAmt",
                        "outWhSaleQtty",
                        "validSaleQtty", "purchaseInAmt", "purchaseInQtty", "purchaseOnwayAmt", "purchaseOnwayQtty",
                        "purchaseOnwayBackQtty", "purchaseOnwayBookQtty", "purchaseValidAmt", "purchaseValidQtty",
                        "returnSuppQtty"],
               "skuId": [df['id'][i]]}

    response = requests.post(
        url=my_url,
        headers=my_json,
        json=my_data
    )
    print('网络状态码', response.status_code)

    # print('响应:', response.text)
    try:
        # data = json.load(f)
        data = response.json()

        for obj2 in data['content']['datas']:
            val = '0'
            city = obj2['rdcCdcName']['name']

            if '.' in obj2['stockQtty']['value']:
                val = obj2['stockQtty']['value'].split('.')[0]

            # print(val)
            # print(city)

            df.loc[i,city] = val

    except json.decoder.JSONDecodeError as e:
        print(e)
        # break

print(str(df))
try:
    df.to_excel('./jd_warehouse.xlsx')
except PermissionError as e:
    print('error:',e)
    df.to_excel(f'./jd_warehouse副本.xlsx')