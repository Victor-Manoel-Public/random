from time import sleep as sl
from pyautogui import typewrite, press


def sendMsg(msg="Hi", times=10):
    while times >= 0:
        typewrite(msg, 0.1)
        press("enter")
        times -= 1

sl(3)
sendMsg()
