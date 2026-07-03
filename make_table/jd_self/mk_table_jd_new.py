import json
import time

import pandas as pd
import requests

from application import request_header

# f = open('a.json','r',encoding='utf-8')

# data = json.load(f)

my_json = request_header.jd_self_header

my_url = 'https://aic.cbbs.tmall.com/aic-report/queryAicInventory'



code_list = ['NKG282','NKG281','HGH2108','HGH2107','HGH2106','HGH2105','SHA2130','SHA2127','SHA2128',
             'SHA2129','TSN2103','TSN2104','WUH2127','WUH2126','CTU2106','CTU2107','512DCAX','','CAN2126',
             'CAN2127','CAN2125','SZX263','SZX264','SZX265']
df3 = pd.DataFrame({
    '仓库CODE': code_list,
    '1003113910434':['','','','','','','','','','','','','','','','','','','','','','','',''],
    '1002493667950':['','','','','','','','','','','','','','','','','','','','','','','','']
})
w_list = [
    '1003113910434',
    '1002493667950',
]
for w_code in w_list:

    print(f'开始运行，仓库代码：{w_code}')
    time.sleep(3)
    my_params = {
        "hideZeroInventory": "1",
        "pageIndex": "1",
        "pageSize": "20",
        "scItemIds": w_code
    }

    response = requests.get(
        url=my_url,
        headers=my_json,
        params=my_params
    )
    print('网络状态码',response.status_code)
    data = response.json()

    for obj in data['data']['dataSource']:
        ipm_num = obj['ipmInventory']['items'][0]['value'] + obj['ipmInventory']['items'][1]['value']
        code_name = obj['storeInfo'].split('\n')[1].split(':')[1]
        print(ipm_num)
        print(code_name)
        df3.loc[df3['仓库CODE'] == code_name, w_code] = ipm_num

df3.to_excel('b_total.xlsx')
