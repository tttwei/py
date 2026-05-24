import json
from datetime import datetime, timedelta

word = ['金香鸭屎+庄园蜜兰','金香鸭屎+清香桂花','庄园鸭屎+岽顶蜜兰香','庄园鸭屎+庄园锯朵仔','购物金',
        '金香鸭屎','庄园鸭屎','庄园蜜兰','岽顶蜜兰香','浓香芝兰','庄园锯朵仔','清香鸭屎','清香桂花','庄园东方红','悠山蜜兰','老丛私房鸭屎香',
        '老丛私房蜜兰香','六大香型300g','六大香型进阶版','四大老丛','老丛私房八仙','老丛私房凹富后','老丛私房宋种','老丛私房东方红',
        '老丛私房姜花香','九大香型','十年陈窖藏鸭屎香','十年陈窖藏蜜兰香']

word_dict = {'金香鸭屎+庄园蜜兰':'鸭屎蜜兰','金香鸭屎+清香桂花':'鸭屎桂花','庄园鸭屎+岽顶蜜兰香':'鸭屎岽顶','庄园鸭屎+庄园锯朵仔':'鸭屎锯朵','购物金':'购物金',
        '金香鸭屎':'金香鸭屎','庄园鸭屎':'庄园鸭屎','庄园蜜兰':'庄园蜜兰','岽顶蜜兰香':'岽顶蜜兰香','浓香芝兰':'浓香芝兰','庄园锯朵仔':'庄园锯朵仔','清香鸭屎':'清香鸭屎','清香桂花':'清香桂花','庄园东方红':'庄园东方红','悠山蜜兰':'悠山蜜兰','老丛私房鸭屎香':'老丛私房鸭屎香',
        '老丛私房蜜兰香':'老丛私房蜜兰香','六大香型300g':'六大','六大香型进阶版':'六大进阶','四大老丛':'四大老丛','老丛私房八仙':'老丛私房八仙','老丛私房凹富后':'老丛私房凹富后','老丛私房宋种':'老丛私房宋种','老丛私房东方红':'老丛私房东方红',
        '老丛私房姜花香':'老丛私房姜花香','九大香型':'九大','十年陈窖藏鸭屎香':'十年陈鸭屎香','十年陈窖藏蜜兰香':'十年陈蜜兰香'}

f = open('Untitled-1.json', 'r', encoding='utf-8')

data = json.load(f)

f.close()

# print(data['mainOrders'][0]['id'])
# print(data['mainOrders'][0]['subOrders'][0]['itemInfo']['skuText'][1]['value'])
# print(data['mainOrders'][0]['orderInfo']['createTime'])
# t1 = data['mainOrders'][0]['orderInfo']['createTime']

# my_time = datetime.strptime(t1,'%Y-%m-%d %H:%M:%S')

# now = datetime.now()
# today_9 = now.replace(hour=9, minute=0, second=0, microsecond=0)
# yesterday_22 = (now - timedelta(days=1)).replace(
#     hour=22,
#     minute=0,
#     second=0,
#     microsecond=0
# )
#
# print(today_9)
# print(yesterday_22)


for obj in data['mainOrders']:
    my_status_code = 0
    # print(obj['id'])
    # print(obj['subOrders'][0]['itemInfo']['skuText'][1]['value'])
    order_id = obj['id']
    try:
        order_value = obj['subOrders'][0]['itemInfo']['skuText'][1]['value']
    except IndexError as e:
        order_value = obj['subOrders'][0]['itemInfo']['skuText'][0]['value']
    order_time = datetime.strptime(obj['orderInfo']['createTime'], '%Y-%m-%d %H:%M:%S')

    # if not yesterday_22 < order_time < today_9:
    #         continue

    print(order_id, end=' ')
    for w in word:
        if w in order_value:
            order_value = word_dict[w]
            my_status_code = 1
            print(order_value)
            break

    if my_status_code == 0:
        print(order_value)


    