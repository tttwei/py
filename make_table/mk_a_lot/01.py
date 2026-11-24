import json
import time
from datetime import datetime, timedelta
from decimal import Decimal

import requests
import pandas as pd


from application import request_header

my_json = request_header.taobao_header
my_json2 = request_header.taobao_dongding_header

today = datetime.now()
# 计算前一天日期
yesterday = today - timedelta(days=1)
# 格式化为字符串
# yesterday_str = "2026-11-21"
yesterday_str = yesterday.strftime("%Y-%m-%d")
print("前一天日期：", yesterday_str)
print("前一天日期：", type(yesterday_str))

# 专属客服
a01_url = (f'https://sycm.taobao.com/qos/customerRelationship/overView.json?dateType=day&dateRange={yesterday_str}%7C{yesterday_str}&'
           f'_=1794924854630&token=fdb4a1cd7')
# my_params01 = ''
# 店铺会员
a02_url = (f'https://sycm.taobao.com/xsite/flagShip/member/overview.json?dateType=day&dateRange={yesterday_str}%7C{yesterday_str}&'
           f'_=1794924854630&token=fdb4a1cd7')

# 淘宝群

# 粉丝群
a03_url = (f'https://sycm.taobao.com/xsite/content/fans/overview.json?dateType=day&dateRange={yesterday_str}%7C{yesterday_str}&'
           f'_=1794924854630&token=fdb4a1cd7')

# 千庭店铺数据
a04_url = (f'https://sycm.taobao.com/flow/v3/source/concerned/shop/v3.json?dateRange={yesterday_str}%7C{yesterday_str}&dateType=day&pageSize=10&page=1&order=desc&orderBy=uv&device=2&belong=all&listT=shopSource7939&randomKey=null&indexCode=uv%2CpayAmt&'
           f'_=1794924854630&token=fdb4a1cd7')
a04_1_url = ('https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2026-11-16%7C2026-11-16&dateType=day&device=0&'
            'token=fdb4a1cd7&_=1794925257050')
# 其他店铺数据
a05_url=(f'https://sycm.taobao.com/mc/mq/rivalShop/analysis/getFlowSource/v3.json?&dateRange={yesterday_str}%7C{yesterday_str}&dateType=day&pageSize=10&page=1&pageType=all&flowBizType=all&marketVersion=free&indexCode=uv&'
         f'rivalUser1Id=RAzN8HWXx11C4gk4uRZiepAAAVGERf5gURWbjqWiiEd5Rweyged&rivalUser2Id=&'
         f'_=1794925046485&token=c204fbb73')

a06_url=(f'https://sycm.taobao.com/mc/mq/rivalShop/analysis/getFlowSource/v3.json?&dateRange={yesterday_str}%7C{yesterday_str}&dateType=day&pageSize=10&page=1&pageType=all&flowBizType=all&marketVersion=free&indexCode=uv&'
         f'rivalUser1Id=RAzN8HWMghydq7ZcKRgWJpyqZUmkzyzb4gGSwNMUxErSXuzjNk9&rivalUser2Id=RAzN8HWUaW9LvwNWicBqEMqdmC13t7gMDNnmeVuDWmYE65arjx5&'
         f'_=1794925046485&token=c204fbb73')
# 店铺id
rivalUser1Id_list = {'RAzN8HWXx11C4gk4uRZiepAAAVGERf5gURWbjqWiiEd5Rweyged':'宋凰',
                     'RAzN8HWMghydq7ZcKRgWJpyqZUmkzyzb4gGSwNMUxErSXuzjNk9':'宏佳',
                     'RAzN8HWUaW9LvwNWicBqEMqdmC13t7gMDNnmeVuDWmYE65arjx5':'净乐'}
# response1 = requests.get(url=a01_url,headers=my_json)
# time.sleep(2)
# response2 = requests.get(url=a02_url,headers=my_json)
# time.sleep(1)
# response3 = requests.get(url=a03_url,headers=my_json)
# time.sleep(2)
# response4 = requests.get(url=a04_url,headers=my_json)
# time.sleep(2)
# response5 = requests.get(url=a05_url,headers=my_json2)
# time.sleep(2)
# response6 = requests.get(url=a06_url,headers=my_json2)
# time.sleep(2)
# 私域好友
def native_friend():
    response1 = requests.get(url=a01_url,headers=my_json)
    time.sleep(1.5)
    print('网络状态码', response1.status_code)

    response2 = requests.get(url=a02_url,headers=my_json)
    time.sleep(1.5)
    print('网络状态码', response2.status_code,response2.json())

    response3 = requests.get(url=a03_url,headers=my_json)
    print('网络状态码', response3.status_code)
    # time.sleep(1)

    # 专属客服
    # print('网络状态码',response1.status_code)
    data1 = response1.json()
    print('累计客户数',data1['data']['totalCustomer']['value'])
    print('累计退订数',data1['data']['totalUnsubscribeCustomer']['value'])
    print('新增退订客户数',data1['data']['addUnsubscribeCustomer']['value'])

    # 店铺会员

    data2 = response2.json()
    # print(data2)
    print('增加会员',data2['content']['data']['newMember']['value'])
    print('会员总数',data2['content']['data']['memberCount']['value'])

    # 粉丝群

    data3 = response3.json()
    print('新增粉丝数',data3['content']['data']['addFansCnt']['value'])
    print('粉丝总数',data3['content']['data']['totalFansCnt']['value'])

    my_dict1={
        '日期':yesterday_str,
        '手动邀请人数': 0,
        '手动增加人数': 0,
        '总增量人数':0,
        '新增退订数量':data1['data']['addUnsubscribeCustomer']['value'],
        '累计退订数量':data1['data']['totalUnsubscribeCustomer']['value'],
        '累计增量专属客服':data1['data']['totalCustomer']['value'],
        '手动邀请':0,
        '每日增量':data2['content']['data']['newMember']['value'],
        '累计增量会员':data2['content']['data']['memberCount']['value'],
        '新增人数':0,
        '累计汇总':0,
        '新增粉丝':data3['content']['data']['addFansCnt']['value'],
        '粉丝汇总':data3['content']['data']['totalFansCnt']['value'],
    }
    df =  pd.DataFrame(my_dict1,index=[0])
    df.to_excel('./output/d1_私人好友.xlsx')

# 千庭店铺数据
# print('网络状态码',response4.status_code)

def taobao_broadcast(data_1,data_2,file_name):
    my_dict = {
        '整体':0,
        '推荐': 0,
        '店铺': 0,
        '宝贝详情': 0,
        '直播关注': 0,
        '广告': 0,
        '搜索': 0,
        '商品点击人数': data_2['data']['self']['broadcastItemClickUv']['value'],
        '成交人数': data_2['data']['self']['broadcastDealUv']['value'],
        '成交金额': data_2['data']['self']['livePlayPayAmt']['value'],
    }
    for i in data_1['data']['data']:
        if i['channelOutName'] in my_dict.keys():
            my_dict[i['channelOutName']] = i['broadcastLookUv']

    pay_amt = str(data_2['data']['self']['livePlayPayAmt']['value'])
    if '.' in pay_amt:
        a_0 = pay_amt.split('.')[0]
        a_1 = pay_amt.split('.')[1]
        my_dict['成交金额'] = a_0 + '.' + a_1[0:2]

    df = pd.DataFrame(my_dict,index=[0])
    df.to_excel(file_name)

def self_shop(data_1,data_2,file_name):
    # f = open('a.json', 'r', encoding='utf-8')
    #
    # data4 = json.load(f)
    #
    # f.close()
    data4 = data_1

    # data4 = response4.json()
    data4_list = data4['data']['data']
    # 手淘搜索	手淘推荐	店铺超链	手淘淘宝直播	我的淘宝	购物车	直通车	引力魔方	万相台
    my_dict = {'手淘搜索': 0,
               '手淘推荐': 0,
               '店铺超链': 0,
               '淘宝直播': 0,
               '我的淘宝': 0,
               '购物车': 0,
               '关键词推广': 0,  # 直通车
               '人群推广': 0,  # 引力魔方
               '智能场景': 0,  # 万相台
               '汇总1':0,
               '日期': yesterday_str,
               '手淘搜索（金额）': 0,
               '手淘推荐（金额）': 0,
               '店铺超链（金额）': 0,
               '淘宝直播（金额）': 0,
               '我的淘宝（金额）': 0,
               '购物车（金额）': 0,
               '关键词推广（金额）': 0,
               '人群推广（金额）': 0,
               '智能场景（金额）': 0,
               '汇总2':0,}
    for i in data4_list:



        if i['pageName']['value'] in my_dict.keys():
            # print(j['pageName']['value'])
            # my_dict[i] = j['uv']['value']
            my_dict[i['pageName']['value']] = i['uv']['value']

            # n2 = i+'（金额）'
            # print(n2)
            pay_amt2 = str(i['payAmt']['value'])
            # if '.' in pay_amt2:
            #     a_0 = pay_amt2.split('.')[0]
            #     a_1 = pay_amt2.split('.')[1]
            #     my_dict[i['pageName']['value'] + '（金额）'] = a_0 + '.' +a_1[0:2]
            # else:
            #     my_dict[i['pageName']['value'] + '（金额）'] = pay_amt2

            my_dict[i['pageName']['value'] + '（金额）'] = Decimal(pay_amt2).quantize(Decimal("0.00"))


    my_dict['汇总1'] = data_2['data']['uv']
    pay_amt = str(data_2['data']['payAmt'])
    if '.' in pay_amt:
        a_0 = pay_amt.split('.')[0]
        a_1 = pay_amt.split('.')[1]
        my_dict['汇总2'] = a_0 + '.' +a_1[0:2]
    else:
        my_dict['汇总2']=pay_amt

    df1 = pd.DataFrame(my_dict, index=[0])
    print(str(df1))
    df1.to_excel(f'./output/d2_{file_name}.xlsx')

# 其他店铺（单一店铺）
def other_shop(data_1,data_2,file_name):
    # f2 = open('test2.json', 'r', encoding='utf-8')

    # data5 = json.load(f2)
    data5 = data_1

    # f2.close()

    # data5 = response5.json()

    my_dict2 = {'手淘搜索': 0,
                '手淘推荐': 0,
                '店铺超链': 0,
                '淘宝直播': 0,
                '我的淘宝': 0,
                '购物车': 0,
                '关键词推广': 0,  # 直通车
                '人群推广': 0,  # 引力魔方
                '智能场景': 0,  # 万相台
                '汇总1':0,
                '日期': yesterday_str,
                '手淘搜索（人数）': 0,
                '手淘推荐（人数）': 0,
                '店铺超链（人数）': 0,
                '淘宝直播（人数）': 0,
                '我的淘宝（人数）': 0,
                '购物车（人数）': 0,
                '关键词推广（人数）': 0,
                '人群推广（人数）': 0,
                '智能场景（人数）': 0,
                '汇总2':0,}
    my_dict2_key_list = ['手淘搜索', '手淘推荐', '店铺超链', '淘宝直播', '我的淘宝', '购物车', '关键词推广', '人群推广',
                         '智能场景']

    def find_by_key(k, mylist):
        for i1 in mylist:
            # print(i1['pageName']['value'])

            # 逻辑
            if i1['pageName']['value'] in my_dict2_key_list:
                if '~' in i1['rivalShop1Uv']['value']:
                    str_arr = i1['rivalShop1Uv']['value'].split('~')
                    my_dict2[i1['pageName']['value']] = (int(str_arr[0]) + int(str_arr[1])) / 2
                else:
                    my_dict2[i1['pageName']['value']] = i1['rivalShop1Uv']['value']

                if '~' in i1['rivalShop1PayByrCnt']['value']:
                    str_arr = i1['rivalShop1PayByrCnt']['value'].split('~')
                    my_dict2[i1['pageName']['value'] + '（人数）'] = (int(str_arr[0]) + int(str_arr[1])) / 2
                else:
                    my_dict2[i1['pageName']['value'] + '（人数）'] = i1['rivalShop1PayByrCnt']['value']

            if k in i1:
                find_by_key(k, i1[k])

    find_by_key('children', data5['data']['data'])

    if '~' in data_2['data']['rivalShop1']['uv']['value']:
        str_arr1 = data_2['data']['rivalShop1']['uv']['value'].split('~')
        my_dict2['汇总1'] = (int(str_arr1[0]) + int(str_arr1[1])) / 2
    else:
        my_dict2['汇总1'] = data_2['data']['rivalShop1']['uv']['value']

    if '~' in data_2['data']['rivalShop1']['payByrCnt']['value']:
        str_arr2 = data_2['data']['rivalShop1']['payByrCnt']['value'].split('~')
        my_dict2['汇总2'] =  (int(str_arr2[0]) + int(str_arr2[1])) / 2
    else:
        my_dict2['汇总2'] = data_2['data']['rivalShop1']['payByrCnt']['value']

    df2 = pd.DataFrame(my_dict2, index=[0])
    df2.to_excel(f'./output/d2_{file_name}.xlsx')

def mk_other_shop():

    for i in rivalUser1Id_list.keys():
        # print(type(i))
        url1 = (f'https://sycm.taobao.com/mc/mq/rivalShop/analysis/getFlowSource/v3.json?dateRange={yesterday_str}%7C{yesterday_str}&'
                f'dateType=day&pageSize=10&page=1&indexCode=uv&'
                f'rivalUser1Id={i}&rivalUser2Id=&device=2&marketVersion=free&'
                f'_=1795004171625&token=4250d5999')
        url2 = (f'https://sycm.taobao.com/mc/mq/rivalShop/analysis/getCoreIndexes.json?dateRange={yesterday_str}%7C{yesterday_str}&'
                f'dateType=day&'
                f'rivalUser1Id={i}&rivalUser2Id=&marketVersion=free&'
                f'_=1795005924885&token=4250d5999')

        res1 = requests.get(url=url1, headers=my_json2)
        time.sleep(1.5)
        print('网络状态码：', res1.status_code, res1.json())

        res2 = requests.get(url=url2, headers=my_json2)
        time.sleep(1.5)
        print('网络状态码：',res2.status_code,res2.json())

        other_shop(res1.json(),res2.json(),rivalUser1Id_list[i])


def mk_self_shop():
    url2 = (
        f'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange={yesterday_str}%7C{yesterday_str}&'
        f'dateType=day&device=0&token=09bad2f69&_=1795007904752')
    res1 = requests.get(url=a04_url, headers=my_json)
    time.sleep(1.5)
    print('网络状态码：', res1.status_code, res1.json())

    res2 = requests.get(url=url2, headers=my_json)
    time.sleep(1.5)
    print('网络状态码：', res2.status_code, res2.json())

    self_shop(res1.json(), res2.json(),'千庭')

def mk_taobao_broadcast():
    url1 = (f'https://sycm.taobao.com/s_content/shop/broadcast/channel/flow/list.json?dateRange={yesterday_str}%7C{yesterday_str}&'
              f'dateType=day&pageSize=10&page=1&order=desc&orderBy=broadcastLookUv&_=1795013705178&token=09bad2f69')
    url2 = (f'https://sycm.taobao.com/s_content/shop/broadcast/click/transform.json?dateType=day&dateRange={yesterday_str}%7C{yesterday_str}&'
            f'_=1795013705166&token=09bad2f69')
    res1 = requests.get(url=url1, headers=my_json)
    time.sleep(1.5)
    print('网络状态码：',res1.status_code,res1.json())

    res2 = requests.get(url=url2, headers=my_json)
    time.sleep(1.5)
    print('网络状态码：', res2.status_code, res2.json())

    taobao_broadcast(res1.json(),res2.json(),'./output/d3_淘宝直播.xlsx')

# 调用
print('调用1...........')
native_friend()
print('调用2...........')
mk_self_shop()
print('调用3...........')
mk_other_shop()
print('调用4...........')
mk_taobao_broadcast()









