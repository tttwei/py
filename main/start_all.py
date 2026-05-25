import os
import threading
import time

dir_path = os.path.dirname(os.path.abspath(__file__))

def exec_file(file_path):
    file_path2 = os.path.join(dir_path,file_path)
    # print(file_path2)
    print(f'运行{file_path.split("/")[2]}')
    os.system(f'python "{file_path2}"')



threading.Thread(target=lambda :exec_file("../click/click_press.py")).start()
time.sleep(0.1)
threading.Thread(target=lambda :exec_file("../press/send_press.py")).start()
time.sleep(0.1)
threading.Thread(target=lambda :exec_file("../send_message/send_message.py")).start()
