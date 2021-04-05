# pip3 install pyautogui
# pip3 install Image
# pip3 install pywinauto

import pyautogui


kakao = pyautogui.locateOnScreen('/Users/sangjin/Desktop/osj/Algorithm-Practice/hobby/chat1.png')
print(kakao)

pyautogui.click(kakao)
pyautogui.click(kakao)

pyautogui.typewrite('오상진', interval=0.1)