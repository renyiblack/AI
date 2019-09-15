import pyautogui


def loot():
    print(">>> Starting looting...")

    pyautogui.keyDown('shift')
    pyautogui.click(button='right', x=770, y=370)  # down
    pyautogui.click(button='right', x=730, y=370)  # left
    pyautogui.click(button='right', x=730, y=320)  # up
    pyautogui.click(button='right', x=730, y=290)  # up
    pyautogui.click(button='right', x=760, y=290)  # right
    pyautogui.click(button='right', x=810, y=290)  # right
    pyautogui.click(button='right', x=810, y=330)  # down
    pyautogui.click(button='right', x=810, y=370)  # down
    pyautogui.keyUp('shift')

    print(">>> Done!")

    pyautogui.moveTo(5, 5)
    print(">>> Moved mouse out of the way!")
