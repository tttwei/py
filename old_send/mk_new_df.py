import pandas as pd

"""
    ⭐
    ⭐需要时间段
"""

# 字段 '订单编号','退款金额','商家备注'
# df = pd.read_excel('./db/order_all.xlsx')
# 字段 主订单编号 商品标题 商品属性
# ⭐
df2 = pd.read_excel('./db/old0708.xlsx')

# df['订单编号'] = df['订单编号'].astype(str)
df2['主订单编号'] = df2['主订单编号'].astype(str)
# df2['订单创建时间'] = pd.to_datetime(df2['订单创建时间'])

# ⭐
start = "2026-06-15 00:00:00"
end = "2026-06-15 23:59:59"

new_df = df2.loc[(df2['订单创建时间'] >= start) & (df2['订单创建时间'] <= end),['主订单编号','订单创建时间','退款金额','商家备注']]
# new_df = df2.loc[0:100,['主订单编号','订单创建时间','退款金额','商家备注']]
new_df.drop_duplicates(subset=['主订单编号'], inplace=True)
new_df['退款金额'] = 0

# (df['时间'] >= start) & (df['时间'] <= end)
# new_df = df['订单编号','退款金额']
print(new_df)

# for k,v in new_df.item():
#     print(k)
#     print(v)
word = ['金香鸭屎+庄园蜜兰','金香鸭屎+清香桂花','庄园鸭屎+岽顶蜜兰香','庄园鸭屎+庄园锯朵仔',
        '金香鸭屎','庄园鸭屎','庄园蜜兰','岽顶蜜兰香','浓香芝兰','庄园锯朵仔','清香鸭屎','清香桂花','庄园东方红','悠山蜜兰','老丛私房鸭屎香',
        '老丛私房蜜兰香','六大香型300g','六大香型进阶版','四大老丛','老丛私房八仙','老丛私房凹富后','老丛私房宋种','老丛私房东方红',
        '老丛私房姜花香','九大香型','十年陈窖藏鸭屎香','十年陈窖藏蜜兰香']

word_price = {
'金香鸭屎+庄园蜜兰':999,'金香鸭屎+清香桂花':999,'庄园鸭屎+岽顶蜜兰香':1499,'庄园鸭屎+庄园锯朵仔':1599,
        '金香鸭屎':888,'庄园鸭屎':1399,'庄园蜜兰':999,'岽顶蜜兰香':1399,'浓香芝兰':888,'庄园锯朵仔':1499,'清香鸭屎':888,'清香桂花':999,'庄园东方红':1399,'悠山蜜兰':369,'老丛私房鸭屎香':1399,
        '老丛私房蜜兰香':1399,'六大香型300g':699,'六大香型进阶版':799,'四大老丛':2099,'老丛私房八仙':1699,'老丛私房凹富后':1699,'老丛私房宋种':2799,'老丛私房东方红':2799,
        '老丛私房姜花香':2799,'九大香型':1099,'十年陈窖藏鸭屎香':2999,'十年陈窖藏蜜兰香':2499,
}

type_list = []
# count1 = 0

def get_max(num_list):
    max_num = 0
    for i in num_list:
        if i > max_num:
            max_num = i

def get_tee_type(tee_list):
    max_tee = tee_list[0]
    for i in tee_list:
        if word_price[i] > word_price[max_tee]:
            max_tee = i
    return max_tee

def take_row(df):
    row_list = []
    # max_tee = '未知类型'
    if not pd.isna(df['商品属性'].iloc[0]):

        for index, row in df.iterrows():
            # print(index)
            # print(row['列名'])
            if not pd.isna(row['商品属性']):
                for w in word:
                    if w in row['商品属性']:
                        row_list.append(w)
                        break
        # row_list.append(row['商品属性'])

    else:
        for index, row in df.iterrows():
            t1 = row['商品标题']
            print(t1)
            try:
                t1 = row['商品标题'].split('【')[1].split('】')[0]
            except IndexError:
                # type_list.append(t1)
                print('=======================出现IndexError异常')
                for w in word:
                    if w in t1:
                        t1 = w
                        break
            print(t1)
            row_list.append(t1)
    # 对比最贵类型
    print('这是rowlist',row_list)
    if len(row_list)>0:
        try:
            max_tee = get_tee_type(row_list)
            return max_tee
        except Exception as e:
            max_tee = row_list[0]
            print('抛出异常',e,'maxtee:',max_tee)
            return max_tee
    else:
        return df['商品属性'].iloc[0]
        # finally:
        #     max_tee = row['商品属性']
        #     return max_tee





for idx, row in new_df.iterrows():
    # print(type(row['订单编号'])) #结果的类型numpy.float64
    order_num = row['主订单编号']
    # print(type(order_num))

    # 筛选出的第一行数据
    row2 = df2.loc[df2['主订单编号'] == order_num]
    print("这是row2================================",row2)
    print(type(row2))

    # the_first_row = row2.iloc[0]
    tee_type = take_row(row2)
    print('这是类型',tee_type)
    type_list.append(tee_type)


    for i in range(len(row2)):
        if df2.loc[df2['主订单编号']==order_num].iloc[i]['退款状态'] == '退款成功':
            new_df.loc[new_df['主订单编号']==order_num,'退款金额'] = 100
            break

    # text = the_first_row['商品属性']
    # print('主订单编号:'+order_num)
    # print(text)

    # if pd.isna(text):
    #     # if '【' not in text:
    #     #     type_list.append(text)
    #     #     continue
    #     t1 = the_first_row['商品标题']
    #     try:
    #         t1 = the_first_row['商品标题'].split('【')[1].split('】')[0]
    #     except IndexError:
    #         # type_list.append(t1)
    #         print('=======================出现IndexError异常')
    #         for w in word:
    #             if w in t1:
    #                 t1 = w
    #                 break
    #
    #     type_list.append(t1)
    #     print(t1)
    #     # print(type_list)
    #     # count1+=1
    #     continue

    # for w in word:
    #     if w in text:
    #         print(w)
    #         type_list.append(w)
    #         # print(type_list)
    #         # count1 += 1
    #         break
    # else:
    #     type_list.append(text)
        # print(type_list)
        # count1 += 1



print('这是new_df长度',len(new_df))
print('list长度',len(type_list))
# print('count1',count1)

new_df['茶叶类型'] = type_list

# print(new_df)
new_df.to_excel('./db/new_df.xlsx')


    # print(newd.iloc[0])
# print(type(df2.iloc[0]['主订单编号']))
# print(type(df2['主订单编号'].iloc[0])) #结果的类型numpy.int64
# print(type(df2.loc[df2['主订单编号']=='3282404340837873861'].iloc[0]['商品属性']))
# print(df2.loc[df2['主订单编号']=='3282404340837873861'].iloc[0]['商品属性'])



