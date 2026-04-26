#!/usr/bin/python3
import time
from tkinter import *

top = Tk()
# 进入消息循环

print(time.strftime("%H:%M:%S"))

def say1():
    s.set('nihao1')

def say2():
    s2.set(time.strftime("%H:%M:%S"))
    s.set('nihao2')

def get_time():

    s2.set(time.strftime("%H:%M:%S"))
    top.after(1000,get_time)

s = StringVar()
s2 = StringVar()
s2.set(time.strftime("%H:%M:%S"))

text1 = Label(top,textvariable=s)
text2 = Label(top,textvariable=s2)

btn1 = Button(top,text='按钮1',command=say1)
btn2 = Button(top,text='按钮2 刷新时间',command=say2)

text1.pack()
text2.pack()
btn1.pack()
btn2.pack()

get_time()

top.mainloop()




