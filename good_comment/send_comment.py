import time

from pynput import keyboard
import pandas as pd
import pyautogui
import pyperclip

# df = pd.read_excel('./db/good_comment.xlsx')
good_comment_df = pd.read_excel('C:\code\python train\good_comment\db\good_comment.xlsx')
def press_1():
    text = good_comment_df['好评'].iloc[0]
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl','v')
    print('老丛杏仁')
def press_2():
    text = good_comment_df['好评'].iloc[1]
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    print('两泡')
def press_3():
    text = good_comment_df['好评'].iloc[2]
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    print('一泡')

# keyboard.add_hotkey('F10',press_1)
# keyboard.add_hotkey('F11',press_2)
# keyboard.add_hotkey('F12',press_3)

h = keyboard.GlobalHotKeys({
    '<f10>': press_1,
    '<f11>': press_2,
    '<f12>': press_3
})

h.start()
h.join()

# keyboard.wait()

