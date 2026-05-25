import json

import pandas as pd
# from streamlit import dataframe

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
}

df = pd.DataFrame(row,index=[0,1,2,3,4,5])

df['id'] = ['100339810862',
'100340414948',
'100339810828',
'100339810826',
'100340414968',
'100339810882']

for i in range(6):
    f = open(f'w{i+1}.json','r',encoding='utf-8')
    # print(f)
    try:
        data = json.load(f)

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
# df.to_excel('./jd_warehouse.xlsx')
