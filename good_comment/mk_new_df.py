import pandas as pd

"""
    ⭐
    ⭐需要时间段
"""

# 字段 '订单编号','退款金额','商家备注'
# df = pd.read_excel('./db/order_all.xlsx')
# 字段 主订单编号 商品标题 商品属性
df2 = pd.read_excel('./db/good0522.xlsx')

# df['订单编号'] = df['订单编号'].astype(str)
df2['主订单编号'] = df2['主订单编号'].astype(str)
# df2['订单创建时间'] = pd.to_datetime(df2['订单创建时间'])

# start = "2026-05-19 00:00:00"
# end = "2026-05-21 23:59:59"

new_df = df2.loc[:,['主订单编号','订单创建时间','退款金额','商家备注']]
# new_df = df2.loc[:100,['主订单编号','订单创建时间','退款金额','商家备注']]
new_df.drop_duplicates(subset=['主订单编号'], inplace=True)
new_df['退款金额'] = 0

# (df['时间'] >= start) & (df['时间'] <= end)
# new_df = df['订单编号','退款金额']
# print(new_df)

# for k,v in new_df.item():
#     print(k)
#     print(v)
word = ['金香鸭屎+庄园蜜兰','金香鸭屎+清香桂花','庄园鸭屎+岽顶蜜兰香','庄园鸭屎+庄园锯朵仔',
        '金香鸭屎','庄园鸭屎','庄园蜜兰','岽顶蜜兰香','浓香芝兰','庄园锯朵仔','清香鸭屎','清香桂花','庄园东方红','悠山蜜兰','老丛私房鸭屎香',
        '老丛私房蜜兰香','六大香型300g','六大香型进阶版','四大老丛','老丛私房八仙','老丛私房凹富后','老丛私房宋种','老丛私房东方红',
        '老丛私房姜花香','九大香型','十年陈窖藏鸭屎香','十年陈窖藏蜜兰香','东方红韵']

type_list = []
# count1 = 0

for idx, row in new_df.iterrows():
    # print(type(row['订单编号'])) #结果的类型numpy.float64
    order_num = row['主订单编号']
    # print(type(order_num))

    # 筛选出的第一行数据
    row2 = df2.loc[df2['主订单编号'] == order_num]
    the_first_row = row2.iloc[0]


    for i in range(len(row2)):
        if df2.loc[df2['主订单编号']==order_num].iloc[i]['退款状态'] == '退款成功':
            new_df.loc[new_df['主订单编号']==order_num,'退款金额'] = 100
            break

    text = the_first_row['商品属性']
    print('主订单编号:'+order_num)
    print(text)

    if pd.isna(text):
        # if '【' not in text:
        #     type_list.append(text)
        #     continue
        t1 = the_first_row['商品标题']
        try:
            t1 = the_first_row['商品标题'].split('【')[1].split('】')[0]
        except IndexError:
            # type_list.append(t1)
            print('=======================出现IndexError异常')
            for w in word:
                if w in t1:
                    t1 = w
                    break

        type_list.append(t1)
        print(t1)
        # print(type_list)
        # count1+=1
        continue

    for w in word:
        if w in text:
            print(w)
            type_list.append(w)
            # print(type_list)
            # count1 += 1
            break
    else:
        type_list.append(text)
        # print(type_list)
        # count1 += 1



print('这是new_df长度',len(new_df))
print('list长度',len(type_list))
# print('count1',count1)

new_df['茶叶类型'] = type_list

print(new_df)
new_df.to_excel('./db/new_df.xlsx')


    # print(newd.iloc[0])
# print(type(df2.iloc[0]['主订单编号']))
# print(type(df2['主订单编号'].iloc[0])) #结果的类型numpy.int64
# print(type(df2.loc[df2['主订单编号']=='3282404340837873861'].iloc[0]['商品属性']))
# print(df2.loc[df2['主订单编号']=='3282404340837873861'].iloc[0]['商品属性'])



