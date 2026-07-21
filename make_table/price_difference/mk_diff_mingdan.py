import pandas as pd
from Demos.win32cred_demo import target

# df = pd.DataFrame({
#     '主订单编号': [],
#     '型号': [],
#     '金额': [],
# })


df2 = pd.read_excel('./old0708.xlsx')

# df['订单编号'] = df['订单编号'].astype(str)
df2['主订单编号'] = df2['主订单编号'].astype(str)

start = "2026-06-22 00:00:00"
end = "2026-06-22 23:59:59"
df = df2.loc[(df2['订单创建时间'] >= start) & (df2['订单创建时间'] <= end),['主订单编号','商家备注']]

# 去重
df.drop_duplicates(subset=['主订单编号'], inplace=True)

df['型号'] = ''
df['退款金额'] = 0

# print(str(df))
target_list = []
target_tee = {
    '老丛私房鸭屎香200g': 1299,
    '老丛私房蜜兰香200g': 1299,
}

def get_type(df):
    pay = 0.0
    tee_list = []
    r = df2.loc[df2['主订单编号'] == df['主订单编号']]
    for idx,row in r.iterrows():
        for w in target_list:
            if w in row['商品属性']:
                p1 = row['买家应付货款'] - target_tee[w]
                if p1 > 0:
                    tee_list.append(w)
                    pay = pay + p1


    return tee_list, pay

for idx,row in df.iterrows():
    if '待发货' in row['商家备注'] or '待 发货' in row['商家备注'] or '待  发货' in row['商家备注'] or '待   发货' in row['商家备注']:
        continue
    t_list,p = get_type(row)

    df.loc[df['主订单编号'] == row['主订单编号'], '型号'] = t_list
    df.loc[df['主订单编号'] == row['主订单编号'], '退款金额'] = p

print(str(df))