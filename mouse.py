import time
import pyautogui as gui

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

bottom = 725
left = 108
top = 41
submenu = 307
subsubmenu = 510

product = point(left, top)
home = point(141, bottom)
login = point(865, top)
menu = point(225, bottom)
start = point(52, bottom)
messages = point(512, bottom)
login_password = point(622, 323)
key_3 = point(244, 347)
key_ok = point(927, 466)
login_ok = point(389, 424)
capture = point(807,864)
hmi = point(760, 0)

def moveClick(target):
    gui.moveTo(target.x, target.y, 1, tween=gui.easeInOutQuad)
    gui.moveTo(target.x, target.y, 1)
    time.sleep(0.1)
    gui.mouseDown()
    time.sleep(0.1)
    gui.mouseUp()
    time.sleep(1)

def MoveHome():
    gui.moveTo(home.x, home.y, 1)

def Home():
    moveClick(home)

def Login():
    moveClick(login)

def Login_Password():
    moveClick(login_password)

def Keyboard_3():
    moveClick(key_3)

def Keyboard_OK():
    moveClick(key_ok)

def Login_OK():
    moveClick(login_ok)

def Menu():
    moveClick(menu)

def RecordStart():
    moveClick(capture)
    time.sleep(2.5)
    moveClick(hmi)
    Home()
    gui.keyDown('shift')
    gui.press('f9')
    gui.keyUp('shift')
    time.sleep(5)

def RecordStop():
    Home()
    time.sleep(2)
    gui.keyDown('shift')
    gui.press('f9')
    gui.keyUp('shift')

def Record(navigation):
    RecordStart()
    navigation()
    RecordStop()