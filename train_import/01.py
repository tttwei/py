# from pynput import keyboard
#
# def start():
#     print("开始")
#
# def stop():
#     print("停止")
#
# h = keyboard.GlobalHotKeys({
#     '<f8>': start,
#     '<f9>': stop
# })
#
# h.start()
# h.join()

try:
    a = 1/2
except Exception as e:
    print('异常',e)
finally:
    print('异常处理完成')

print('执行中')