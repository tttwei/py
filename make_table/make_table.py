import pandas as pd
import datetime
# df = pd.DataFrame(columns=['申请日期','登记人','订单编号','旺旺','退货明细截图','退款金额','退货单号','物流进度','是否完成退款'])
df1 = pd.DataFrame(columns=['登记时间','淘宝or天猫','订单号','买家会员名','寄件人信息','型号规格*数量','退货OR换货','退换货原因','退回快递单号','退款金额'])
# print(df)
# df.to_excel('./t1.xlsx')
df = pd.read_excel('./t1.xlsx')
df['订单编号'] = df['订单编号'].astype(str)
# print(excel)
# print(df.to_string())
# print(df.loc[df['退货单号'] == '顺丰速运 SF5199883700753'])

# 按照指定格式输出当前日期和时间
my_now_date = datetime.datetime.now().strftime('%m月%d日')
print(my_now_date)

f = open('relay.txt', 'r', encoding='utf-8')
readline = f.readline()
while readline:
    my_list = []
    # order_num = df[]
    str_array = readline.replace("\n", "").split('，',1)
    # 退货单号
    s1 = str_array[0].split('、')[1]
    # 退货明细
    s2 = str_array[1]
    print(s1)
    print(s2)
    # 退货or换货
    s3 = '退货'

    # row = df.loc[s1 in df['退货单号']]
    # print(row)
    for index,row in df.iterrows():
        if s1 in row['退货单号']:
            if row['退款金额'] == 0:
                s3 = '换货'
            my_list = [my_now_date, '天猫', row['订单编号'],row['旺旺'],'',s2,s3,'口感不合适',s1,row['退款金额'],]
            df1.loc[len(df1)] = my_list
    # print(my_list)
    # print(len(my_list))
    if not len(my_list) == 10:
        print('=============================',s1,'找不到')
    readline = f.readline()



df1.to_excel('./tuihuo_table.xlsx')