from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
from PIL import Image

resolusi = pyautogui.size()
XMata = int(resolusi[0]*0.75)
YMata = int(resolusi[1]*0.6)
BXMata = int(resolusi[0]*1)
BYMata = int(resolusi[1]*1)
# Initialize Resolusi Yang Digunakan Oleh User

time.sleep(5)
# Beri Waktu Buat Load Library

starttime = time.time()
# Buat Ngitung Waktu Yang Dihabiskan Buat Mancing


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# Function buat click di defined X Koordinat dan Y Koordinat

totalikan = 0
# Variabel Buat Ngitung Berapa Banyak Ikan Yang Didapet

while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('target.png', region=(XMata, YMata, BXMata ,BYMata), confidence=0.8) != None:
        click(int(resolusi[0] * 0.85),int(resolusi[1] * 0.73))
        print("Berhasil Menangkap Ikan")
        totalikan = totalikan+1
        print("Total Ikan Terpancing = ",totalikan," Ikan.")
        time.sleep(6)
        click(int(resolusi[0] * 0.85),int(resolusi[1] * 0.73))
        
endtime = time.time() - starttime

print ("Memancing Selama %.0f Detik." % endtime)
