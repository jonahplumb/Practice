import pyautogui
import time

time.sleep(3)
# Opening our windows search bar, typing Valorant and pressing enter
pyautogui.hotkey('winleft')
pyautogui.typewrite('Valorant\n', 0.5)
# This pause could be shorter but dependent on PC hardware the riot client can 
# take a few moments to load
time.sleep(8)
# Delete the #Username & #Password and enter your Username and Password,
pyautogui.typewrite(#Username\t") #Entering our username 
pyautogui.typewrite(#Password\n") #Entering our password
  
time.sleep(2)
pyautogui.click(x=372,y=911)
# Allow Valorant to load, then clicking in the lower right
# of our screen to avoid the mouse-glitch which has been a bug in Valorant for some time
time.sleep(8)
pyautogui.click(x=1887,y=809)
