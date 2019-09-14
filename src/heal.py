import pyautogui


# these settings are made for 1366x768, change x,y if in other resolution, possibly needs to change rgb too

def HealLowLVL():
    if not (pyautogui.pixelMatchesColor(1237, 310, (255, 113, 113))):  # life bar(status) ~30%
        pyautogui.press('f1')  # [3 line from bot to top]
        print(">>> using life pot...")
    else:
        if not (pyautogui.pixelMatchesColor(1284, 310, (255, 113, 113))):  # life bar(status) ~80%
            pyautogui.press('f3')  # [3 line from bot to top]
            print(">>> healing...")
        if not (pyautogui.pixelMatchesColor(1260, 323, (116, 113, 255))):  # mana bar(status) 30%
            # [3 line from bot to top]
            pyautogui.press('f2')
            print(">>> using mana pot...")


def HealRook():
    if not (pyautogui.pixelMatchesColor(1237, 310, (255, 113, 113))):  # life bar(status) ~30%
        pyautogui.press('f1')  # [3 line from bot to top]
        print(">>> using life pot...")
