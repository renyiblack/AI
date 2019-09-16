import pyautogui
import time


def loot():
    offset_x = 270
    offset_y = 180
    distance_x = 40
    distance_y = 40

    print(">>> Starting looting...")

    pyautogui.keyDown('shift')
    pyautogui.click(button='right', x=770 + offset_x, y=370 + offset_y)  # down
    time.sleep(0.5)
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=370 + offset_y)  # left
    time.sleep(0.5)
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=320 + offset_y - distance_y)  # up
    time.sleep(0.5)
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=290 + offset_y - distance_y)  # up
    time.sleep(0.5)
    pyautogui.click(button='right', x=770 + offset_x, y=290 + offset_y - distance_y)  # right
    time.sleep(0.5)
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=290 + offset_y - distance_y)  # right
    time.sleep(0.5)
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=320 + offset_y - distance_y)  # down
    time.sleep(0.5)
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=370 + offset_y)  # down
    time.sleep(0.5)
    pyautogui.keyUp('shift')

    print(">>> Done!")

    pyautogui.moveTo(5, 5)
    print(">>> Moved mouse out of the way!")
