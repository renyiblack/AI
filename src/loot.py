import pyautogui


def loot():

    # X, Y offset between 1920x1080(21:9) to 1366x768(16:9), to use this code on 1366x768 change offsets to 0
    # Distance is the offset between tiles

    offset_x = 270
    offset_y = 180
    distance_x = 40
    distance_y = 40

    print(">>> Starting looting...")

    pyautogui.keyDown('shift')
    pyautogui.click(button='right', x=770 + offset_x, y=370 + offset_y)  # down
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=370 + offset_y)  # left
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=320 + offset_y - distance_y)  # up
    pyautogui.click(button='right', x=730 + offset_x - distance_x, y=290 + offset_y - distance_y)  # up
    pyautogui.click(button='right', x=770 + offset_x, y=290 + offset_y - distance_y)  # right
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=290 + offset_y - distance_y)  # right
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=320 + offset_y - distance_y)  # down
    pyautogui.click(button='right', x=810 + offset_x + distance_x, y=370 + offset_y)  # down
    pyautogui.keyUp('shift')

    print(">>> Done!")

    pyautogui.moveTo(5, 5)
    print(">>> Moved mouse out of the way!")
