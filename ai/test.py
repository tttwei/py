# from ai.ne import amount
from user_model import User
from decimal import Decimal, ROUND_HALF_UP
import pymysql
from datetime import datetime

from painting_model import Painting

# # 初始金额10000
# user = User(10000)
# '2016-01-04', '2016-01-05', '2016-01-06',
# '2016-01-07', '2016-01-08', '2016-01-11',
# '2016-01-12', '2016-01-13', '2016-01-14',
# '2016-01-15',
'''
# start_time = '2020-01-01'
# end_time = '2024-01-01'
# day =  40
# 模式
# type = 1


# 银行，半导体，证券，电力行业，食品饮料，汽车，保险，消费电子，酒
bk_list =[]
if type==0:
    bk_list = ['bk0475', 'bk1036','bk0473','bk0428','bk0438','bk1029','bk0474','bk1037','bk0477']
elif type==1:
    bk_list = ['ixic','hk']
    '''
# bk_list = ['bk0475']
# bk_list = ['bk0422', 'bk0730', 'bk0733', 'bk0738', 'bk1016', 'bk0482', 'bk0734',
#            'bk0450', 'bk0731', 'bk0424', 'bk0484', 'bk0465', 'bk0451', 'bk0732',
#            'bk1042', 'bk0539', 'bk0740', 'bk0475', 'bk0421', 'bk1039', 'bk0476',
#            'bk1029', 'bk1040', 'bk0538', 'bk1043', 'bk0433', 'bk0454', 'bk0427',
#            'bk0728', 'bk1041', 'bk0425', 'bk0474', 'bk1045', 'bk0436', 'bk0438',
#            'bk0546', 'bk0726', 'bk1028', 'bk1044', 'bk1019', 'bk0478', 'bk1036',
#            'bk0735', 'bk0725', 'bk0437', 'bk1020', 'bk0473', 'bk1015', 'bk0464',
#            'bk0440', 'bk1035', 'bk0479', 'bk1038', 'bk1032', 'bk0729', 'bk0481',
#            'bk0456', 'bk0477', 'bk0737', 'bk0470', 'bk1031', 'bk0471', 'bk0458',
#            'bk0428', 'bk0429', 'bk0420', 'bk0447', 'bk1046', 'bk0457', 'bk0910',
#            'bk0480', 'bk0448', 'bk1037', 'bk0727', 'bk1030', 'bk0459', 'bk1018',
#            'bk1017', 'bk0486', 'bk1027', 'bk0736', 'bk0545', 'bk1033', 'bk0739',
#            'bk0485', 'bk1034']


# 创建连接
conn = pymysql.connect(host='localhost', user='root', password='123456', database='machine_trading', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

#最早日期判断，判断是否可用，存在就参与统计，不存在跳过
def get_first_time(bk_name):
    sql = f"select 日期 from {bk_name} limit 1"
    cursor.execute(sql)
    obj = cursor.fetchall()
    return obj[0][0]

def compare_time(bk_name,now_time):
    first_time = get_first_time(bk_name)
    f_date = datetime.strptime(str(first_time), "%Y-%m-%d")
    n_date = datetime.strptime(now_time, "%Y-%m-%d")

    return n_date >= f_date


def get_price_by_date(bk_name1,date1):
    sql = f"select 收盘 from {bk_name1} where 日期 = '{date1}'"

    cursor.execute(sql)
    obj = cursor.fetchall()
    price = obj[0][0]
    return price


# print(get_price_by_date('ixic', '2016-01-04'))
# 0是国内，1是国外
def get_time_list(s,e,type):
    if type == 0:
        sql = f"select 日期 from bk0475 where 日期 >= '{s}' and 日期 <= '{e}'"
    elif type == 1:
        sql = f"select l.日期 from ixic ,(select hk.日期 from gold,hk where hk.日期 = gold.日期 and hk.日期<='{e}' and hk.日期>='{s}') l where l.日期 = ixic.日期"
    cursor.execute(sql)
    obj = cursor.fetchall()
    date_list = []
    for i in obj:
        date_list.append(i[0])
    # print(date_list)
    return date_list
def get_bkname_by_code(code):
    sql = f"select 板块名称 from bkmap where 板块代码 = '{code}'"
    cursor.execute(sql)
    obj = cursor.fetchall()
    return obj[0][0]


# print(get_bkname_by_code('bk0475'))
# print(get_time_list())
# print(len(get_time_list()))


def run(bk_list,day,s,e,type):
    # paint_x = get_time_list()
    # 参数供调整
    user = User(10000)

    paint_x = []
    paint_y = []

    s_index = Decimal('0')
    e_index = Decimal('0')

    total = len(get_time_list(s,e,type))
    date_list = get_time_list(s,e,type)
    # print(date_list)
    # 时间指针
    t1 = ''

    # 计数器
    counter = 0
    bk_map = {}
    # page = 0
    # 步长标尺
    n = 0

    max_code = ''
    growth_rate = Decimal('-99999')
    last_growth_rate = Decimal('-99999')

    while True:
        for bk_name in bk_list:

            t1 = date_list[n]

            # print(t1)
            if (len(bk_list) == 1 and not compare_time(bk_name, t1)):
                return {
                    'paint_x' : [],
                    'paint_y' : [],
                    'amount':-999999

                }

            if not compare_time(bk_name,t1) :continue

            open_price = get_price_by_date(bk_name, t1)

            if bk_name not in bk_map:
                # 第一次直接记录价格到字典中
                bk_map[bk_name] = open_price
            else:

                new_growth_rate = (Decimal(str(open_price))-Decimal(str(bk_map[bk_name])))/Decimal(str(bk_map[bk_name]))
                n1 = (new_growth_rate*100).quantize(Decimal('0.00000'), rounding=ROUND_HALF_UP)
                # print(f'{t1} {bk_name}增长率{n1}')

                if new_growth_rate > growth_rate:
                    growth_rate = new_growth_rate
                    max_code = bk_name

                bk_map[bk_name] = open_price



        # print(f'{t1}查看last_growth_rate：{last_growth_rate}')
        if counter==1:
            # 把s价格填入
            s_index = get_price_by_date(max_code, t1)
            if n + day <= total - 1:
                e_index = get_price_by_date(max_code, date_list[n+day])
        elif counter>=2:
            # print('sIndex和eIndex',end='')
            # print(s_index, e_index)

            if last_growth_rate >= 0:
                # 交易
                r = user.change_amount(s_index, e_index)

            # 把s价格填入
            s_index = get_price_by_date(max_code, t1)
            if n+day <= total-1:
                e_index = get_price_by_date(max_code, date_list[n+day])


        # print(f'现在账户余额{user.amount}')
        # 绘制
        paint_y.append(float(user.amount))
        # 绘制
        paint_x.append(t1)
        # print('===================这是第'+str(counter)+'次===================')

        counter += 1
        last_growth_rate = growth_rate

        if n+day > total-1 :
            # print("结束")
            # print("共有",get_total(),"天交易日")
            break
        n += day
        # page += day
        growth_rate = Decimal('-99999')
    return {
        'paint_x':paint_x,
        'paint_y':paint_y,
        'amount':user.amount
    }



# run(bk_list,day,type)


# painting.run(get_time_list(type)[0],day,type)
# 查全部板块均日
def main():
    start_time = '2024-01-01'
    end_time = '2025-01-01'
    day =  7
    # 模式
    type = 0

    l2 = get_time_list(start_time,end_time,type)

    # 选择起点
    # date_list = get_time_list(start_time, end_time, type)
    # print(date_list)
    # 加2000，24913，不加26522
    # 16-25，不加41573，加2000，37465
    # 银行，半导体，证券，电力行业，汽车，保险，消费电子，酒
    bk_list = []
    if type == 0:
        # bk_list = ['bk0475', 'bk1036', 'bk0473', 'bk0428', 'bk1029', 'bk0474', 'bk1037', 'bk0477','sh932000']
        # bk_list = ['sh000016','sh932000']
        # bk_list = ['sh159941']
        # bk_list = ['sh159941','bk0475', 'sh159934']
        bk_list = ['bk1016', 'bk0422', 'bk0730', 'bk0733', 'bk0738', 'bk0482', 'bk0734',
                   'bk0450', 'bk0731', 'bk0424', 'bk0484', 'bk0465', 'bk0451', 'bk0732',
                   'bk1042', 'bk0539', 'bk0740', 'bk0475', 'bk0421', 'bk1039', 'bk0476',
                   'bk1029', 'bk1040', 'bk0538', 'bk1043', 'bk0433', 'bk0454', 'bk0427',
                   'bk0728', 'bk1041', 'bk0425', 'bk0474', 'bk1045', 'bk0436', 'bk0438',
                   'bk0546', 'bk0726', 'bk1028', 'bk1044', 'bk1019', 'bk0478', 'bk1036',
                   'bk0735', 'bk0725', 'bk0437', 'bk1020', 'bk0473', 'bk1015', 'bk0464',
                   'bk0440', 'bk1035', 'bk0479', 'bk1038', 'bk1032', 'bk0729', 'bk0481',
                   'bk0456', 'bk0477', 'bk0737', 'bk0470', 'bk1031', 'bk0471', 'bk0458',
                   'bk0428', 'bk0429', 'bk0420', 'bk0447', 'bk1046', 'bk0457', 'bk0910',
                   'bk0480', 'bk0448', 'bk1037', 'bk0727', 'bk1030', 'bk0459', 'bk1018',
                   'bk1017', 'bk0486', 'bk1027', 'bk0736', 'bk0545', 'bk1033', 'bk0739',
                   'bk0485', 'bk1034']
    elif type == 1:
        bk_list = ['ixic', 'hk']


    l1 = []
    # 计数器
    c=1
    # 选择最优秀板块
    nbBK_map = {}
    nb_list =[]
    # while day <=20:
    for i2 in bk_list:
        all_m = 0
        tem_list = [i2]
        for i in range(day):

            paint_obj = run(tem_list, day,l2[i],end_time, type)



            # paint_x = paint_obj['paint_x']
            # paint_y = paint_obj['paint_y']
            a = paint_obj['amount']
            all_m+=a

            # print(paint_x)
            # print(paint_y)
            # painting = Painting(paint_x, paint_y)
            # painting.run(get_time_list(l2[i],end_time,type)[0],day,type)
        ave = all_m/day
        ave = int(ave)

        nbBK_map[i2] = ave
        nb_list.append(ave)

        print(f"序号{c},{i2},{day}日周期，均收益{ave}")
        c+=1
    print(nbBK_map)
    nb_list.sort(reverse=True)
    print(nb_list)
    for i in nb_list:
        key = next((k for k, v in nbBK_map.items() if v == i), None)

        print(get_bkname_by_code(key),end=' ')
        print(key,end=' ')
        print(i)

# main()
# 查单日
def main2():
    start_time = '2018-01-01'
    end_time = '2020-01-01'
    day = 7
    # 模式
    type = 0

    l2 = get_time_list(start_time, end_time, type)

    # 选择起点
    date_list = get_time_list(start_time, end_time, type)
    # print(date_list)

    # 银行，半导体，证券，电力行业，食品饮料，汽车，保险，消费电子，酒,纳指
    bk_list = []
    if type == 0:
        # bk_list = ['sh159941','bk0475', 'bk1036', 'bk0473']
        bk_list = ['bk0420','bk0448','bk0736','bk0735','bk0728']
    elif type == 1:
        bk_list = ['ixic', 'hk']

    # for i in range(2):
    # s_time = date_list[i]

    paint_obj = run(bk_list, day, start_time, end_time, type)

    paint_x = paint_obj['paint_x']
    paint_y = paint_obj['paint_y']
    print(paint_x)
    print(paint_y)
    painting = Painting(paint_x, paint_y)
    painting.run(get_time_list(start_time,end_time,type)[0],day,type)

# main2()
# print(user.amount)
# 查均日
def main3():
    start_time = '2025-04-29'
    end_time = '2025-09-13'
    # 20==9,34====7,26
    # 16==7,32==9,39
    day = 7
    # 模式
    type = 0

    l2 = get_time_list(start_time, end_time, type)

    # 选择起点
    date_list = get_time_list(start_time, end_time, type)
    print(date_list)
    # 加2000，24913，不加26522
    # 16-25，不加41573，加2000，37465
    # 银行，半导体，证券，电力行业，汽车，保险，消费电子，酒
    bk_list = []
    if type == 0:
        # bk_list = ['bk0475', 'bk1036', 'bk0473', 'bk0428', 'bk1029', 'bk0474', 'bk1037', 'bk0477','sh932000']
        # bk_list = ['bk0475', 'bk0473', 'bk0428', 'bk0474'] # 银行，证券，电力，保险
        # bk_list = ['sh000016','sh932000']
        # bk_list = ['sh159941']
        # 不缓冲12916,加15295
        # bk_list =['bk0727','bk0733','bk0480','bk0465','bk0729']
        # bk_list = ['bk0475', 'bk0473', 'bk0428', 'bk0474','sh159934','sh159941','etf159920']        # 银行，证券，电力，保险，黄金，纳指，恒生
        # bk_list = ['etf512880', 'etf512800', 'etf167301', 'etf159611', 'sh159934', 'etf159941', 'etf159920'] # 银行，证券，保险，电力，黄金，纳指，恒生
        #
        # bk_list = ['etf512880', 'etf512800', 'etf167301', 'etf159611','sh159934', 'etf159941', 'etf159920']
        bk_list = ['etf167301','etf159941','etf512800','etf512880','etf159611','etf159920','etf159934']
    elif type == 1:
        bk_list = ['ixic', 'hk']

    l1 = []

    all_m = 0
    for i in range(day):
        paint_obj = run(bk_list, day, l2[i], end_time, type)

        paint_x = paint_obj['paint_x']
        paint_y = paint_obj['paint_y']
        a = paint_obj['amount']
        all_m += a

        print(paint_x)
        print(paint_y)
        painting = Painting(paint_x, paint_y)
        painting.run(get_time_list(l2[i],end_time,type)[0],day,type)
    ave = all_m / day
    ave = int(ave)



    print(f"{day}日周期，均收益{ave}")
main3()


