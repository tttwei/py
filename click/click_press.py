import os
import threading

import pyautogui
from pynput import keyboard
# import keyboard
'''

'''
dir_path = os.path.dirname(os.path.abspath(__file__))

qianniu3_path = os.path.join(dir_path,'img','qianniu3.png')

def to_click1():
    print('触发了')
    x, y = pyautogui.locateCenterOnScreen(qianniu3_path,region= (597, 1142,703,58), confidence=0.9)
    pyautogui.click(x, y,duration=0.1)
    # print(x,y)

    pyautogui.click(x+172, y-108,duration=0.3)
    pyautogui.click(1362,695,duration=0.1)

def to_click2():
    print('触发了')
    x, y = pyautogui.locateCenterOnScreen(qianniu3_path,region= (597, 1142,703,58), confidence=0.9)
    pyautogui.click(x, y,duration=0.1)
    # print(x,y)

    pyautogui.click(x+172, y-108,duration=0.2)
    pyautogui.moveTo(707, 275, duration=0.1)
# keyboard.add_hotkey('F4',to_click)

def on_f4():
    threading.Thread(target=to_click1).start()
def on_f3():
    threading.Thread(target=to_click2).start()
h = keyboard.GlobalHotKeys({
    '<f4>': on_f4,
    '<f3>': on_f3
})

h.start()
h.join()

# keyboard.wait()