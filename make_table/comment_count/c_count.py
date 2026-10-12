import json

from pandas import DataFrame

f = open('c.json','r',encoding='utf-8')

c=0

data = json.load(f)

df = DataFrame({
'100339810882':	'云顶鸭屎200g',
'100340414968':	'云顶蜜兰200g',
'100339810826':	'经典鸭屎200g',
'100339810828':	'云顶鸭屎100g',
'100340414948':	'云顶蜜兰100g',
'100339810862':	'经典鸭屎100g',
'100369453694':	'臻品单丛200g',
'100349174078':	'经典鸭屎7g',
'100349174076':	'云顶蜜兰7g',
'汇总1': '汇总1',
'100386109594':	'雅韵鸭屎210g',
'100386109556':	'雅韵蜜兰210g',
'100296695761':	'沁香鸭屎210g',
'100386109616':	'沁香蜜兰210g',
'100386109536':	'山叙鸭屎210g',
'100296695733':	'山叙蜜兰210g',
'100315085277':	'焖丛鸭屎30g+焖泡杯480ml',
'100410249140':	'焖丛蜜兰30g+焖泡杯480ml',
'100315085301':	'开茶见喜42g',
'100391289446':	'沁香鸭屎7g',
'100391289448':	'山叙鸭屎7g',
'汇总2': '汇总2',
},index=[0,1])

for i in range(len(data['data']['data'])):
    for j in range(len(data['data']['data'][i]['skuInfoVOList'])):
        skuId = data['data']['data'][i]['skuInfoVOList'][j]['skuId']
        skuCount = data['data']['data'][i]['skuInfoVOList'][j]['commentSummaryVO']['commentCount']
        print(skuId)
        df.loc[1,str(skuId)] = skuCount
        # print(skuCount)
        c += 1


        # print('计数：',c)

df['汇总1'] = df.iloc[1, 0:9].sum()
#
print(df.loc[1,'汇总1'])

df['汇总2'] = df.iloc[1, 10:21].sum()
#
print(df.loc[1,'汇总2'])

# print(str(df))
df.to_excel('./count.xlsx')
    # for obj in data['data']['dataSource']:

# df3.to_excel('c_total.xlsx')
