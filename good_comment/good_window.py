import time
from tkinter import *
import pandas as pd
import pyautogui
import pyperclip
from pynput import keyboard

df = pd.read_excel('./db/new_df.xlsx')
# push_df = pd.read_excel('./db/customer_push_table.xlsx')
df['商家备注'] = df['商家备注'].astype(str)
good_comment_df = pd.read_excel('C:\code\python train\good_comment\db\good_comment.xlsx')

# 设置窗口样式
top = Tk()
top.geometry('300x200')
top.title('good')

# 索引，当前位置
i = 0
# 状态码
status_code = 0

# 设置变量
order_number = StringVar()
type_tee = StringVar()
index_var = StringVar()


# 数据初始化函数 2 red,1 yellow,0 white
def change(idx):
    global status_code
    row = df.iloc[idx]
    order_number.set(row['主订单编号'])
    type_tee.set(row['茶叶类型'])
    index_var.set(idx)
    if '待发货' in row['商家备注'] or '待 发货' in row['商家备注']:
        top.config(bg='red')
        status_code = 2
        return 2
    elif row['退款金额'] > 0:
        top.config(bg='yellow')
        status_code = 1
        return 1
    else:
        top.config(bg='white')
        status_code = 0
        return 0

def previous_order():
    global i
    if i > 0:
        i -= 1
    s = change(i)
    # top.config(bg='yellow')
    print('调用上一个')
    return s

def next_order():
    global i
    if i < len(df)-1:
        i += 1
    s = change(i)
    # top.config(bg='red')
    print('调用下一个')
    return s


def press_1():
    text = good_comment_df['好评'].iloc[0]
    pyperclip.copy(text)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl','v')
    print('老丛杏仁')
    next_order()

def press_2():
    text = good_comment_df['好评'].iloc[1]
    pyperclip.copy(text)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    print('两泡')
    next_order()

def press_3():
    text = good_comment_df['好评'].iloc[2]
    pyperclip.copy(text)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    print('一泡')
    next_order()



change(0)

l1 = Label(top,textvariable=order_number)
l1.pack()
l2 = Label(top,textvariable=type_tee)
l2.pack()
l3 = Label(top,textvariable=index_var)
l3.pack()

btn1 = Button(top,text='上一个',command=previous_order)
btn1.pack()
btn2 = Button(top,text='下一个',command=next_order)
btn2.pack()



# keyboard.add_hotkey('F10',press_1)
# keyboard.add_hotkey('F11',press_2)
# keyboard.add_hotkey('F12',press_3)

h = keyboard.GlobalHotKeys({
    '<f10>': press_1,
    '<f11>': press_2,
    '<f12>': press_3
})

h.start()


mainloop()

