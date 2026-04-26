import threading
import time
# from cProfile import label
# from threading import Thread
from tkinter import *

# from Demos.win32cred_demo import target
from pynput import mouse,keyboard
import pyautogui


# 限定搜索区域 (left, top, width, height)701,240 820,1034
region = (330, 253, 78, 782)

# (763, 403)点击位置
# 330，253
# 408，1035
# 1041底部位置
top_y_point = 0

status_code = True

top = Tk()
top.geometry('400x200')
top.title('click_work')
top.config(bg='white')

x1 = IntVar()
mouse_xy = StringVar()
mouse_xy.set('未赋值')
# time.sleep(3)
# matches = pyautogui.locateAllOnScreen('./img/t5.png', region=region, confidence=0.8)

def get_mouse():
    x, y = pyautogui.position()
    mouse_xy.set(f'({x}, {y})')
    x1.set(x)
    print(f"鼠标当前位置: ({x}, {y})")

def set_status_code():
    global status_code

    if status_code:
        status_code = False
        top.config(bg='red')
    else:
        return
    time.sleep(2)
    status_code = True
    top.config(bg='white')

# 连续点击
def click_1(matches,my_click_x):
    # 转成列表（很重要，不然是生成器）
    # print(list(matches))
    global top_y_point
    matches_list = list(matches)
    # print(matches_list[0].top)
    top_y_point = matches_list[0].top
    reversed_list = sorted(matches_list, reverse=True)
    for r in reversed_list:
        if not status_code:
            break
        center = pyautogui.center(r)
        pyautogui.click(my_click_x, center.y, duration=0.5)
        # print(center) # 输出中心点坐标 (x, y)

# 点完连续翻页
def main(x):
    print(x)
    print(type(x))
    if x == 0:
        print('请输入x值')
        return
    while True:
        # try:
        matches = pyautogui.locateAllOnScreen('./img/t5.png', region=region, confidence=0.8)
        click_1(matches, x)
        if not status_code:
            break
        #
        # except Exception as e:
        #     print('======================出现异常',e)
        #     return
        # print(top_y_point)
        print(1024 - top_y_point)
        pyautogui.scroll(int(1041 - top_y_point))

        if int(1024 - top_y_point) < 600:
            break

        time.sleep(0.5)

# def listener():
def press_f10():
    threading.Thread(target=get_mouse).start()

def press_f11():
    threading.Thread(target=set_status_code).start()


h = keyboard.GlobalHotKeys({
    '<F10>':press_f10,
    '<F11>':press_f11
})
h.start()

# thread2 = threading.Thread(target=listener)
# thread2.start()

# while True:
#     s = int(input())
#     print(type(s))
#     print(s)
#     main(s)
l1 = Label(top,text='自动点击，F10看坐标F11暂停')
l1.pack()
l2 = Label(top, textvariable= mouse_xy)
l2.pack()
e1 = Entry(top, textvariable=x1)
e1.pack()

b1 = Button(top,text='运行',command=lambda : main(x1.get()))
b1.pack()

mainloop()



