# import pyautogui

# x, y = pyautogui.locateCenterOnScreen('./wx.png', confidence=0.9)
# pyautogui.moveTo(x, y, duration=0.5)
# pyautogui.click()
# pyautogui.write('hejiajun1shi1baichi1',interval=0.1)
# pyautogui.press("enter")
# print(x,y)
# pyautogui.displayMousePosition()
# (763, 403)
# 330，253
# 408，1035
from pynput import mouse
import time

def on_move(x, y):
    # 处理鼠标移动事件，输出当前坐标
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    # 当鼠标点击事件发生时，输出点击的信息
    if not pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        # 当鼠标点击事件发生且松开时，退出监听
        return False

def on_scroll(x, y, dx, dy):
    # 当鼠标滚轮事件发生时，输出滚轮的信息
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# 设置鼠标监听器
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
