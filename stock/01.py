import akshare as ak
import pandas as pd
from sqlalchemy import create_engine

# # 显示所有列
# pd.set_option('display.max_columns', None)
# # 显示所有行
# pd.set_option('display.max_rows', None)
# # 防止内容被省略
# pd.set_option('display.expand_frame_repr', False)

#
bk_list = ['BK0422', 'BK0730', 'BK0733', 'BK0738', 'BK1016', 'BK0482', 'BK0734',
           'BK0450', 'BK0731', 'BK0424', 'BK0484', 'BK0465', 'BK0451', 'BK0732',
           'BK1042', 'BK0539', 'BK0740', 'BK0475', 'BK0421', 'BK1039', 'BK0476',
           'BK1029', 'BK1040', 'BK0538', 'BK1043', 'BK0433', 'BK0454', 'BK0427',
           'BK0728', 'BK1041', 'BK0425', 'BK0474', 'BK1045', 'BK0436', 'BK0438',
           'BK0546', 'BK0726', 'BK1028', 'BK1044', 'BK1019', 'BK0478', 'BK1036',
           'BK0735', 'BK0725', 'BK0437', 'BK1020', 'BK0473', 'BK1015', 'BK0464',
           'BK0440', 'BK1035', 'BK0479', 'BK1038', 'BK1032', 'BK0729', 'BK0481',
           'BK0456', 'BK0477', 'BK0737', 'BK0470', 'BK1031', 'BK0471', 'BK0458',
           'BK0428', 'BK0429', 'BK0420', 'BK0447', 'BK1046', 'BK0457', 'BK0910',
           'BK0480', 'BK0448', 'BK1037', 'BK0727', 'BK1030', 'BK0459', 'BK1018',
           'BK1017', 'BK0486', 'BK1027', 'BK0736', 'BK0545', 'BK1033', 'BK0739',
           'BK0485', 'BK1034']
bk_list = ['167301','159941','512800','512880','159611','159920','159934']
# 创建数据库引擎（使用 pymysql 连接器）
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/machine_trading')

# for bk_name in bk_list:
#     print("开始导入板块代码为："+bk_name)
    # df = ak.stock_board_industry_hist_em(symbol=bk_name,
    #                                  start_date="20160101",
    #                                  end_date="20250422",
    #                                  period="日k",
    #                                  adjust="qfq")
# df = ak.stock_zh_a_hist(symbol="512690", period="daily", start_date="20240101", end_date='20250422',
#                                         adjust="qfq")

# = ak.stock_board_industry_hist_em(symbol="小金属", start_date="20211201", end_date="20240222", period="日k", adjust="")
# import akshare as ak
# 银行，半导体，证券，电力行业，食品饮料，汽车，保险，消费电子，酒
# 酒etf,保险lof,汽车etf,证券etf,半导体etf,银行etf,电力etf,消费电子etf,,,,,,,,,,
# etf_list = ['512690','167301','159512','512880','512480','159611','159732']

fund_etf_hist_em_df = ak.fund_etf_hist_em(symbol="167301", period="daily", start_date="20250428", end_date="20250913", adjust="qfq")
print(fund_etf_hist_em_df)
df = ak.stock_board_industry_hist_em(symbol='BK0475',
                                 start_date="20250428",
                                 end_date="20250913",
                                 period="日k",
                                 adjust="qfq")
df.to_sql('bk0475', con=engine, index=False, if_exists='append')
'''
for i in bk_list:
    df = ak.fund_etf_hist_em(symbol=i, period="daily", start_date="20250428", end_date="20250913", adjust="qfq")
    # print(fund_etf_hist_em_df)
    # print(stock_zh_a_hist_df)
    print("获取akShare api数据......")
    print(df)
    # 写入到数据库中的表（如果表存在就替换）
    # df.to_sql(i.replace('BK','bk'), con=engine, index=False, if_exists='replace')
    df.to_sql('etf'+ i , con=engine, index=False, if_exists='append')
'''
# print(ak.stock_board_industry_name_em())
# ak.stock_board_industry_name_em().to_sql('bkmap', con=engine, index=True)


# # or 'append'
# df = ak.index_zh_a_hist(symbol="000016", period="daily", start_date="20160101", end_date="22220101")
# df.to_sql(f"sh000016", con=engine, index=False)
# print(df)
# , if_exists='replace'

# df = ak.fund_etf_hist_em(symbol="000001", period="daily", start_date="20090101", end_date="20250610", adjust="qfq")
# # df['日期']
# df.to_csv('上证0925.csv', index=False, encoding='gbk')
# print(df)
# df.to_sql('etf159611',con=engine, index=False)