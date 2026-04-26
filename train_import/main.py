# import A.AA.a
import keyboard

from A.AA import a
from B import b
# A.AA.a.eat()
# a.eat()
# b.sleep()
# a.weizhi()

keyboard.add_hotkey('1',a.eat)
keyboard.add_hotkey('2',a.eat)

keyboard.wait()