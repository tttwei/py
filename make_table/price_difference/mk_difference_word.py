import os

import pandas as pd

dir_path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_excel('a.xlsx')
# df['退价格'] = df['退价格'].astype(str)

# print(df.loc[0:10,['名字','型号','退价格']])
# print('长度：',len(df))

def add_str(array):
    s = ''
    for i in range(len(array)):
        if i == len(array) - 1:
            s = s + '【' + array[i] + '】'
        else:
            s = s + '【' + array[i] + '】' + '\n'
    return s

for idx, row in df.iterrows():
    print(row['名字'],'=========',row['订单号'],row['型号'],row['退价格'])

    p1 = str(row['退价格'])
    if p1.split('.')[1] == '0':
        p1 = p1.split('.')[0]

    # print(type(p1))
    print('--------------------')
    # 多单
    if '\n' in row['型号']:
        str_array = row['型号'].split('\n')
        s1 = add_str(str_array)
        # print('测试1：',s1)
        print(f'''亲亲 非常感谢您对千庭的支持/:809
 前两天您在咱们店铺购买了
{s1}
狂暑季活动您购买有官方直降12%优惠（您当时购买官方直降10%） 
您现在购买的订单整单计算价格会比超级88活动价高【{p1}】元
咱们想给您同步狂暑季活动价哈
这边给您推送退差价链接
退款金额已给您设置【{p1}】元
您点击下方链接即可退差价/:Q
PS1：另外咱们给您退完差价之后 您狂暑季活动再查看一下哈 如果发现到手价比咱们给您退差价后到更低  您截图给咱们 咱们给您继续退差价处理哈
PS2：如果口感满意，麻烦您帮忙晒2张美照哈''')
    else:
        # print('')
        # 单订单
        print(f'''亲亲 非常感谢您对千庭的支持/:809
 前两天您在咱们店铺购买了
      【{row['型号']}】
价格会比狂暑季活动价高【{p1}】元
咱们想给您同步狂暑季活动价哈
这边给您推送一个退差价链接
退款金额已给您设置【{p1}】元
您点击下方链接即可退差价/:Q
PS1：另外咱们给您退完差价之后 您狂暑季活动再查看一下哈 如果发现到手价比咱们给您退差价后到更低  您截图给咱们 咱们给您继续退差价处理哈
PS2：如果口感满意，麻烦您帮忙晒2张美照哈''')
    print('=============================')
    print()
