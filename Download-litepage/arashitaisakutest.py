import pyautogui
import time
import sys
time.sleep(2)
print(pyautogui.position())
pyautogui.click(1380,990)
while True:
    pyautogui.typewrite("korehaarasitaisakunotesutodesu")
    time.sleep(0.1)
    pyautogui.press("enter")
sys.exit