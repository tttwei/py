import os
import threading
import time
import sys
from datetime import datetime
from tkinter import *
from tkinter import ttk

import pyautogui
import pyperclip


# special_case_array = ['鸭屎蜜兰','鸭屎桂花','鸭屎锯朵','鸭屎岽顶','六大','六大进阶']
special_dict = {
    '鸭屎蜜兰':'亲亲  您刚刚下单的这款是咱们的浓淡组合装，里面有鸭屎香和蜜兰香，这两款香型口感也是非常不错的哈，您付款',
    '鸭屎桂花':'您刚刚下单的这款是咱们的高香组合装，里面有鸭屎香和桂花香，',
    '鸭屎锯朵':'您刚刚下单的这款组合装，里面有高山鸭屎香和高山锯朵仔，',
    '鸭屎岽顶':'您刚刚下单的这款是咱们的乌岽高山组合装',
    '悠山蜜兰':'您拍的这款悠山蜜兰丨头春头采，蜜韵甘甜，您付款',
    '六大':'您拍的这款六大组合丨六大香型茶集，',
    '六大进阶':'您拍的这款六大组合丨六大香型茶集进阶版',
    '九大':'您拍的这款九大组合丨九大香型茶集，品味9种美味，您付款',
    '金香鸭屎':'亲亲 ，您拍的这款金香鸭屎丨头春头采，回甘十足，您付款后咱们联系仓库给您优先安发货哈',
    '清香鸭屎':'亲亲 ，您拍的这款清香鸭屎丨头春头采，回甘十足，您付款',
    '浓香芝兰':'亲亲 ，您拍的这款浓香芝兰丨头春头采，花香浓郁，您付款后咱们联系仓库给您优先安发货哈',
    '庄园蜜兰': '亲亲 ，您拍的这款庄园蜜兰丨头春头采，蜜韵甘甜，您付款后咱们联系仓库给您优先安发货哈',
    '清香桂花':'亲亲 ，您拍的这款清香桂花丨桂花香韵，甜润顺滑，您付款后咱们联系仓库给您优先安排发货哈',
    '庄园鸭屎':'亲亲 ，您拍的这款庄园鸭屎丨茶韵十足，奶香浓郁，您付款后咱们联系仓库给您优先安发货哈',
    '岽顶蜜兰香':'亲亲 ，您拍的这款岽顶蜜兰香丨头春头采，蜜韵甘甜，您付款后咱们联系仓库给您优先发货哈',
    '庄园东方红':'亲亲 ，您拍的这款庄园东方红丨回甘猛烈，醇和顺滑，您付款后咱们联系仓库给您优先安发货哈',
    '庄园锯朵仔':'亲亲 ，您拍的这款庄园锯朵仔丨杏仁果韵，柔棉香甜，您付款后咱们联系仓库给您优先安排发货哈',
    '十年陈蜜兰香':'您拍的这款十年陈窖藏蜜兰香，',
    '十年陈鸭屎香':'您拍的这款十年陈窖藏鸭屎香，',
    '四大老丛':'您拍的这款四大老丛丨乌岽核心产区，一杯倾心，一口爱上，您付款',
    '老丛私房鸭屎香':'您拍的这款老丛私房鸭屎丨获特等金奖，乌岽核心产区，回甘十足，您付款',
    '老丛私房蜜兰香':'您拍的这款老丛私房蜜兰丨乌岽核心产区，珍贵名丛，蜜韵甘甜，您付款',
    '老丛私房八仙':'您拍的这款老丛私房八仙丨乌岽核心产区，珍贵名丛，醇和甘爽，您付款',
    '老丛私房东方红':'您拍的这款老丛私房东方红丨乌岽核心产区，百年树龄，香韵独特，您付款',
    '老丛私房宋种':'您拍的这款老丛私房宋种丨乌岽核心产区，百年树龄，花香浓密，您付款',
    '老丛私房凹富后':'您拍的这款老丛私房凹富后，是老丛庄园茶 也是珍贵名丛 ，特别适合资深老茶客，口感很不错哈，您付款',
    '老丛私房姜花香':'您拍的这款老丛私房姜花香，是老丛庄园茶 也是珍贵名丛 ，特别适合资深老茶客，口感很不错哈，您付款',
    '购物金':'您可以充值下咱们的购物金哈，充值1500得1600，充值3000得3300哈，您可以充值后下单',
}

top = Tk()
top.geometry('400x200')
# top.config(bg='white')
top.title('send_message')

s1 = StringVar()
s2 = StringVar()


dir_path = os.path.dirname(os.path.abspath(__file__))

# 浏览器位置


def my_send_msg(order_num,tee_type):
    # num = '2701754007048029192'
    # 1
    edge_path = os.path.join(dir_path,'img','edge.png')
    x, y = pyautogui.locateCenterOnScreen(edge_path, region=(597, 1142, 703, 58), confidence=0.9)
    # x, y = pyautogui.locateCenterOnScreen('./img/edge.png', confidence=0.7)
    # print(datetime.now())
    # if order_num == '' or tee_type == '':
    #     print('请填入数值')
    #     return
    # print(order_num,tee_type)

    pyautogui.click(x, y, duration=0.3)

    pyautogui.click(428,26,duration=0.2)
    pyautogui.moveTo(464, 528, duration=0.2)
    pyautogui.scroll(1200)
    pyautogui.click(duration=0.2)
    pyautogui.click(810,660,duration=0.2)
    time.sleep(0.1)
    # sys.exit(0)
    # pyautogui.write(num,interval=0.1)
    pyautogui.click()
    pyperclip.copy(order_num+'')
    pyautogui.hotkey("ctrl", "v")

    pyautogui.click(1692,1083,duration=0.2)

    pyautogui.click(620,554,duration=0.2)
    pyautogui.scroll(-720)

    pyautogui.click(620,284,duration=0.2)


    pyautogui.click(620,500,duration=0.5)


    pyperclip.copy(special_dict[tee_type])


    pyautogui.hotkey("ctrl", "v")

    pyautogui.click(889,484,duration=0.2)


    pyautogui.click(1475,672,duration=2)

    pyautogui.click(1789,1070,duration=0.2)

    # time.sleep(0.5)
    # pyautogui.moveTo(869,719,duration=1)
    # # 截图
    # pyautogui.keyDown('shift')
    # pyautogui.scroll(-690)
    # pyautogui.keyUp('shift')
    # pyautogui.screenshot('../screenshot/屏幕截图_'+str(time.time()).replace('.', '_')+'.png', region=(383, 644, 1448, 173))

    pyautogui.click(x, y, duration=0.5)


# 读取文件
def together_read():
    a_path = os.path.join(dir_path,'a.txt')
    f = open(a_path, 'r', encoding='utf-8')
    readline = f.readline()
    while readline:
        str_array = readline.replace("\n","").split(' ')

        my_send_msg(str_array[0], str_array[1])

        # print(str_array[0],str_array[1])
        readline = f.readline()

def one_send():
    my_send_msg(s1.get(),s2.get())
def all_send():
    threading.Thread(target=together_read).start()

Label(top,text='订单').pack()
e1 = Entry(top,textvariable=s1)
e1.pack()
Label(top,text='类型').pack()
# e2 = Entry(top,textvariable=s2)
# e2.pack()


cmb = ttk.Combobox(top, textvariable=s2)

cmb['values'] = (
    '金香鸭屎',
    '清香鸭屎',
    '庄园鸭屎',
    '庄园蜜兰',
    '岽顶蜜兰香',
    '购物金',
    '庄园东方红',
    '庄园锯朵仔',
    '浓香芝兰',
    '清香桂花',

    '悠山蜜兰',
    '六大',
    '六大进阶',
    '九大',
    '四大老丛',

    '十年陈蜜兰香',
    '十年陈鸭屎香',

    '老丛私房鸭屎香',
    '老丛私房蜜兰香',
     '老丛私房八仙',
    '老丛私房东方红',
     '老丛私房宋种',
    '老丛私房凹富后',
    '老丛私房姜花香',
    '鸭屎蜜兰',
    '鸭屎桂花',
    '鸭屎锯朵',
    '鸭屎岽顶',

)

cmb.current(0)  # 默认选中第一个

cmb.pack()


b1 = Button(top,text='批量发送',command=all_send)
b1.pack(side="left",ipadx=5, padx=20)
b2 = Button(top,text='单一发送',command=one_send)
b2.pack(side="right",ipadx=20, padx=30)

mainloop()
