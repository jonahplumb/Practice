import pyautogui
import time

#Not needed just here so that the user has moment of pause 
time.sleep(3)
#Following commands are opening our windows search bar, typing Valorant and pressing enter
#This will gurantee it works, no matter where you have Valorant downloaded
pyautogui.hotkey('winleft')
pyautogui.typewrite('Valorant\n', 0.5)

#This pause could be shorter but dependent on PC hardware the riot client can 
# take a few moments to load
time.sleep(8)
#Entering our username and password for the valorant account followed by pressing enter
#Delete the #Username & #Password and enter your Username and Password,
pyautogui.typewrite(#Username\t")
pyautogui.typewrite(#Password\n")
#Sometimes to right client requires players to press "Play"
#Dependent on 1920x1080
time.sleep(2)
pyautogui.click(x=372,y=911)
#This is a breif pause to allow Valorant to load, then clicking in the lower right
# of our screen to avoid the mouse-glitch which has been a bug in Valorant for some time
time.sleep(8)
pyautogui.click(x=1887,y=809)
