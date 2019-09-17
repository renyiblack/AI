import pyautogui
import time

from src.imagesearch import imagesearcharea


def spells(coord1, coord2):
    global n
    # 527,805
    if n == 0:
        pyautogui.press('f8')
        time.sleep(.03)
    if imagesearcharea("exori.png", 527, 803, 527, 803):
        # if(n==0): pyautogui.press('f8')
        pyautogui.press('f5')
        n = n + 1
    # n=n+1
    else:
        if imagesearcharea("exoriGran.png", 601, 802, 601, 802):
            pyautogui.press('f7')
            n = n + 1
    if n == 8:
        n = 0
