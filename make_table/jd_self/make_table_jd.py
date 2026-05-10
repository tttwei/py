import pandas as pd

df = pd.read_excel('./b1.xlsx')
df2 = pd.read_excel('./b2.xlsx')

# print(df['仓库CODE'])
# print(df['IPM可售'])
code_list = ['NKG282','NKG281','HGH2108','HGH2107','HGH2106','HGH2105','SHA2130','SHA2127','SHA2128','SHA2129','TSN2103','TSN2104','WUH2127','WUH2126','CTU2106','CTU2107','512DCAX','','CAN2126','CAN2127','CAN2125','SZX263','SZX264','SZX265']
"""
500g庄园鸭屎：1003113910434	500g金香鸭屎：1002493667950

NKG282,NKG281,HGH2108,HGH2107,HGH2106,HGH2105,SHA2130,SHA2127,SHA2128,SHA2129,TSN2103,TSN2104,WUH2127,WUH2126,CTU2106,CTU2107,512DCAX,,CAN2126,CAN2127,CAN2125,SZX263,SZX264,SZX265
"""
df3 = pd.DataFrame({
    '仓库CODE': code_list,
    '500g庄园鸭屎：1003113910434':['','','','','','','','','','','','','','','','','','','','','','','',''],
    '500g金香鸭屎：1002493667950':['','','','','','','','','','','','','','','','','','','','','','','','']
})
# df1['仓库CODE'] = df['仓库CODE']

for idx,row in df.iterrows():
    print(row['仓库CODE'])
    # print(row.loc[0,'仓库CODE'])
    df3.loc[df3['仓库CODE'] == row['仓库CODE'],'500g庄园鸭屎：1003113910434'] = row['IPM可售']

for idx,row in df2.iterrows():
    print(row['仓库CODE'])
    # print(row.loc[0,'仓库CODE'])
    df3.loc[df3['仓库CODE'] == row['仓库CODE'], '500g金香鸭屎：1002493667950'] = row['IPM可售']

df3.to_excel('b_total.xlsx')
