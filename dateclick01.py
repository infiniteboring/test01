import pyautogui
import time
while True:

 time1 = list(time.localtime())  # 获取本地时间

 hour1 = time1[3]

 minute1 = time1[4]
 if hour1 == 20 and minute1 == 40:
   pyautogui.moveTo(917, 830, duration=0.1)
   pyautogui.click()
   break



