# import sys
#
# # print(sys.argv)
# f = open('a.txt','r',encoding='utf-8')
# readline = f.readline()
# while readline:
#     s = readline.replace("\n","").split(' ')
#
#     print(s[0],s[1],end='')
#     readline = f.readline()
# newstr = readline.replace('\n','')
# print(newstr,end="")
import time

import pyautogui
from tornado.gen import sleep

# s1 = '你好'
# s2 = '你好'
# print(s1 == s2)
# arr = ['nihao','a','b','c']
#
# print('a' in arr)
# print('a'.find(arr))
# special_dict = {
#     '鸭屎蜜兰':'鸭屎蜜兰',
#     '鸭屎桂花':'鸭屎桂花',
#     '鸭屎锯朵':'鸭屎锯朵',
#     '鸭屎岽顶':'您刚刚下单的这款是咱们的乌岽高山组合装'
# }
# print(special_dict['鸭屎岽顶'])

time.sleep(3)
# 截图
# pyautogui.keyDown('shift')
pyautogui.scroll(1200)
# pyautogui.keyUp('shift')
# pyautogui.screenshot('./screenshot/屏幕截图_'+str(time.time()).replace('.', '_')+'.png', region=(383, 644, 1448, 173))
# # print(str(time.time()).replace('.',''))

a = '【优惠价】【重磅新品】千庭岽顶蜜兰香凤凰单枞茶叶 潮州乌岽高山单丛500g,【优惠价】【新品】千庭单丛 老丛宋种 乌岽高山特级凤凰单枞茶礼盒100g,【岽顶蜜兰香】品鉴装7g,千庭单丛老丛私房宋种品鉴装小金罐7g,【取茶3件套】茶则丨茶拨丨茶巾'
print('岽顶蜜兰' in a)