import pandas as pd
from decimal import Decimal

df2 = pd.read_excel('e2.xlsx')

# df['订单编号'] = df['订单编号'].astype(str)
df2['主订单编号'] = df2['主订单编号'].astype(str)

start = "2026-06-22 00:00:00"
end = "2026-06-22 23:59:59"
# df = df2.loc[(df2['订单创建时间'] >= start) & (df2['订单创建时间'] <= end),['主订单编号','商家备注']]
df = df2.loc[:,['主订单编号','商家备注']]
# 去重
df.drop_duplicates(subset=['主订单编号'], inplace=True)

df['型号'] = ''
df['退款金额'] = '0'
# print(str(df))

# print(str(df))
target_list = []
target_tee = {
    '金香鸭屎500g':838,
    '庄园鸭屎500g':1299,
    '老丛私房鸭屎香200g': 1299,
    '老丛私房蜜兰香200g': 1299,
    '庄园东方红500g': 1299,
    '岽顶蜜兰香500g': 1299,
    '庄园蜜兰500g': 949,
    '清香桂花500g': 949,
    '浓香芝兰500g': 838,
    '庄园锯朵仔50g': 175.12,
    '庄园东方红50g': 165.44,
    '庄园鸭屎50g': 165.44,
    '岽顶蜜兰香50g': 165.44,
    '庄园蜜兰50g': 121.44,
    '清香桂花50g': 121.44,
    '清香鸭屎50g': 112.64,
    '浓香芝兰50g': 112.64,
    '金香鸭屎50g': 112.64,
}
# 初始化列表
for k in target_tee:
    # print(k)
    target_list.append(k)
# print(target_list)
def get_type(df):
    pay = Decimal('0')
    # pay = 0.0
    tee_list = []
    r = df2.loc[df2['主订单编号'] == df['主订单编号']]
    for idx,row in r.iterrows():

        if pd.isna(row['商品属性']):
            continue

        # print(row['买家应付货款'])
        # print(type(row['买家应付货款']))
        # print(row['商品属性'])

        for w in target_list:
            if w in row['商品属性']:
                # print(row['商品属性'])
                # print(row['买家应付货款'])
                # print(type(row['买家应付货款']))
                p1 = Decimal(str(row['买家应付货款'])) - Decimal(str(target_tee[w])) * Decimal(str(row['购买数量']))
                if p1 > 0:
                    tee_list.append(w+'*'+str(row['购买数量']))
                    pay = pay + p1
                break


    return tee_list, pay

for idx,row in df.iterrows():
    if not pd.isna(row['商家备注']):
        if '待发货' in row['商家备注'] or '待 发货' in row['商家备注'] or '待  发货' in row['商家备注'] or '待   发货' in row['商家备注']:
            continue

    t_list,p = get_type(row)

    # print(row['主订单编号'])
    # print(type(row['主订单编号']))
    # print(df.iloc[1]['主订单编号'])
    # print(type(df.iloc[1]['主订单编号']))
    # # print(df.index)
    # break
    type_str = ''
    total = len(t_list)
    c2 = 0
    for t1 in t_list:
        if total == 1:
            type_str = t1
        else:
            if c2 == total - 1:
                type_str = type_str + t1
            else:
                type_str = type_str + t1 + '\n'
        c2 = c2 + 1

    df.loc[df['主订单编号'] == row['主订单编号'], '型号'] = type_str
    df.loc[df['主订单编号'] == row['主订单编号'], '退款金额'] = str(p)

print(df.to_string())
df = df[df['退款金额'] != '0']
df.to_excel('./df.xlsx')