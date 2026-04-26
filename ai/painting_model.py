import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


class Painting:

    # 示例数据
    x = []
    y = []

    def __init__(self,x,y):
        self.x = pd.to_datetime(x)
        self.y = y

    def run(self,t,day,type):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, marker='o', linestyle='-', color='b', label='price')

        ax.set_title(f"{t},{day}day")
        ax.set_xlabel('type:'+str(type))
        ax.set_ylabel('price')

        # x轴只显示年月（可按需改为'%Y-%m-%d'）
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        # 自动旋转日期标签
        fig.autofmt_xdate()

        ax.grid(True)
        ax.legend()

        # plt.savefig(f'{day}日.png', dpi=300, bbox_inches='tight')

        plt.show()


