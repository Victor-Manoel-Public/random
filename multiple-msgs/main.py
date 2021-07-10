from time import sleep as sl
from pyautogui import typewrite, press

# this code can send multiples messages to multiples text messengers (WhatsApp, Instagram, Facebook, Telegram, etc).

def sendMsg(msg="Hi", times=10): # creates the function with 2 parameters
    while times >= 0: # while this condition is true, send the messages and hit the "enter" button.
        typewrite(msg, 0.1) # same as pyautogui.typewrite().
        press("enter") # same as pyautogui.press().
        times -= 1 # here we decrement the times the messages timer.

sl(3) # wait 3 seconds before the program begin.
sendMsg() # here we call our funcion without any parameters (). By defalut, the program will send "Hi" 10 times.

