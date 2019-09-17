import pyautogui
import time

'''
        To use on 1366x768(16:9) set offset to 0
        To use on 1920x1080(21:9) set offset_x to 270, offset_y to 180, distance_x to 40 and distance_y to 40

        Remember to change params on main.py and heal.py too
'''


def loot():
    offset_x = 0        # 270
    offset_y = 0        # 180
    distance_x = 0      # 40
    distance_y = 0      # 40

    print(">>> Starting looting...")

    pyautogui.keyDown('shift')
    pyautogui.click(button='right', x=770 + offset_x, y=370 + offset_y)                             # down
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=370 + offset_y)                # left
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=320 + offset_y - distance_y)   # up
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=290 + offset_y - distance_y)   # up
    pyautogui.click(button='right', x=770 + offset_x, y=290 + offset_y - distance_y)                # right
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=290 + offset_y - distance_y)   # right
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=320 + offset_y - distance_y)   # down
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=370 + offset_y)                # down
    pyautogui.keyUp('shift')

    print(">>> Done!")

    pyautogui.moveTo(5, 5)
    print(">>> Moved mouse out of the way!")
