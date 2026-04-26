# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from decimal import Decimal
#
# # a = input("按下 enter 键退出，其他任意键显示...\n")
# #
# # b=10
# # a='abcde'
# # # print (b,end=" ")
# # # print('www' + 'op')
# # print(a[1:-2])
# #
# # for x in range(5):
# #     print(x)
# pin = Decimal('0')
# for i in range(2):
# #     pin = Decimal('908')
# #
# # print(pin)
# from datetime import datetime
#
# date1 = datetime.strptime("2012-12-12", "%Y-%m-%d")
# date2 = datetime.strptime("2020-12-03", "%Y-%m-%d")
# # print(obj[])
# if date1 >= date2:
#     print("1111")
# else:
#     print("2222")
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
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="159941", period="daily", start_date="20170301", end_date='20240528', adjust="qfq")
print(stock_zh_a_hist_df)