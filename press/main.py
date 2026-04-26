from good_comment import send_comment
import send_press_old
import keyboard



# keyboard.add_hotkey('F6', send_comment.start_send_F6)
keyboard.add_hotkey('F7', send_press.stop_text)
#
keyboard.add_hotkey('F10',send_comment.press_1)
# keyboard.add_hotkey('F11',press_2)
# keyboard.add_hotkey('F12',press_3)
keyboard.wait()
