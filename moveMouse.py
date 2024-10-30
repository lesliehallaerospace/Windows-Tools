import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = False
num_sec = 60
a = 0   
logoff = (60*8.32)
print("started")
while a < logoff:
    x = 0

    while x < num_sec:
        time.sleep(1)
        x += 1

    x, y = pyautogui.position()
    pyautogui.moveTo(x + 10, y + 10)
    pyautogui.moveTo(x, y)
    pyautogui.press("shift")

    print("Movement made at {}".format(datetime.now().time()))

    a += 1