import threading
import time

import keyboard
import pyautogui
import pyperclip
from tkinter import *

# time.sleep(3)
# 1为禁止发送
status_code = 0

top = Tk()
top.geometry('300x200')

press_text_list=[
    '您付款后和咱们说下，我和仓库说下，给您安排优先发货哈/:Q',
    '咱们家的订单会比较多哈 您拍下后和我这边说下哈   咱们通知仓库 给您优先安排发货哈/:803',
    '您拍下后跟咱这边说下哈，咱这边通知仓库给您安排妥当发出哈/:809',
    '咱们是广东的凤凰单丛茶原产地哈，口感非常不错，您可以试一下哈/:809',
    '咱们有加赠一泡同款茶样给您试喝哈/:087',
    '您收到货，先试喝一下品鉴装哈，如果口感不合适，正装不开封，咱们支持7天无理由退货退款的哈/:087',
    '咱们现在发货的是2025年的春茶哈，您购买正装咱们有加赠同款品鉴装，您收到货可以先品鉴一下口感合不合口哈/:809',
    '咱们家是正宗的广东凤凰单丛茶原产地，口感好喝，您可以试一下哈/:803',
    '亲亲 咱们现在是活动价 您购买的话非常划算 不要错过了哈/:803',
    '咱们家的乌龙茶是广东的凤凰单丛，既有红茶的甜，又有绿茶的香，还有自有的回甘，口感很不错，您可以购买品尝一下哈/:809',
    '不用担心买贵哈，咱们买贵支持退差价的哈/:087',
    '咱们还有加赠同款品鉴装哈  亲亲如果收到货试喝口感不满意的话  正装不拆封的话  咱们是支持7天无理由退货哈/:803',
    '您到时先试喝下品鉴装哈/:Q',
    '咱们现在是活动价哈，您购买品尝更划算/:809',
    '口感不用担心哈，咱家购买正装会有加赠同款的品鉴装试喝哈，亲亲收到货先试喝品鉴装哈，好喝在拆封正装/:087',
    '您付款后，赠品会随单发出哈/:Q',
    '喜欢可以下单哈，我联系仓库给您优先顺丰发出哈/:803',
    '亲亲，鸭屎香是单丛茶的代表香，人称茶中香水，口感非常不错哈，您付款后跟我说下，咱们联系仓库给您优先发货哈/:803',
    '亲亲，口感不用担心哈，咱家购买正装会有加赠同款的品鉴装试喝哈，亲亲收到货先试喝品鉴装哈，好喝在拆封正装/:071',
    '亲亲 ，咱们家的乌龙茶是广东的凤凰单丛，既有红茶的甜，又有绿茶的香，还有自有的回甘，口感不错，您可以试一下哟/:071',
    '亲亲 您这边有什么顾虑可以跟咱这边说下哈 ，咱专注单丛 只做单丛 ，在乌岽山自建庄园一体化种茶制茶，也得到过许多茶友的认可哈，口感跟质量都值得保证哈/:803',
    '亲亲 咱们千庭专注单丛  只做单丛  口感不错哈 亲亲可以试一下哈/:Q',
    '亲亲 咱们千庭种植园是在凤凰山脉乌岽山哈 是正宗的原产地 口感不错哈/:803',
    '亲亲 咱们千庭专注单丛 只做单丛 口感不错哈 亲亲可以试一下哈/:071',
    '亲亲 咱们千庭专注做单丛茶的哈 在乌岽山自建茶庄园 口感上您不用担心哈 咱家购买正装会加赠同款品鉴装哈/:803',
]

def change(code):
    global status_code
    if code == 1:
        status_code = 1
        top.config(bg='red')
    elif code == 0:
        status_code = 0
        top.config(bg='white')

def send_text():
    i = 1
    for text in press_text_list:
        if status_code == 1:
            print('禁止状态不能发送')
            return

        print('连续发送',i)
        i = i+1
        pyperclip.copy(text)
        # time.sleep(0.2)

        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('enter')

        time.sleep(1)

def start_send_F6():
    t = threading.Thread(target=send_text)
    t.start()

def stop_text():
    print('停止')
    change(1)

def reset():
    print('恢复')
    change(0)


l1 = Label(top,text='F6发送 F7停止')
l1.pack()

btn1 = Button(top,text='发送',command=start_send_F6)
btn1.pack()
btn2 = Button(top,text='停止',command=stop_text)
btn2.pack()
btn3 = Button(top,text='恢复',command=reset)
btn3.pack()



keyboard.add_hotkey('F6', start_send_F6)
keyboard.add_hotkey('F7', stop_text)

mainloop()