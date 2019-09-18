import pyautogui
from src.imagesearch import imagesearcharea

# TODO make this work

def sell_loot(starter_mark, img, map_x, map_y, map_x1, map_y1, offset_pos_x1, offset_pos_x2):
    sell_x = 329
    sell_y = 64

    center_to_sell_x = 199
    center_to_sell_y = 98

    max_x = 285
    max_y = 191

    ok_x = 321
    ok_y = 223

    coord_1, coord_2 = imagesearcharea(img[starter_mark], map_x, map_y, map_x1, map_y1)
    pos_x = map_x + coord_1 + 3
    pos_y = map_y + coord_2 + 3

    while not pos_x < offset_pos_x1 or pos_x > offset_pos_x2 or pos_y < 81 or pos_y > 83:
        print(">>> Moving...")
        pyautogui.click(pos_x, pos_y)
        pyautogui.moveTo(5, 5)
        print(">>> Moved mouse out of the way")

    pyautogui.click(button='right', x=770, y=328)

    starter_mark = 0

    coord_1, coord_2 = imagesearcharea(img[starter_mark], map_x, map_y, map_x1, map_y1)
    pos_x = map_x + coord_1 + 3
    pos_y = map_y + coord_2 + 3

    while not pos_x < offset_pos_x1 or pos_x > offset_pos_x2 or pos_y < 81 or pos_y > 83:
        print(">>> Moving...")
        pyautogui.click(pos_x, pos_y)
        pyautogui.moveTo(5, 5)
        print(">>> Moved mouse out of the way")

    pyautogui.typewrite('hi', interval=0.25)
    pyautogui.press('enter')
    pyautogui.typewrite('trade', interval=0.25)
    pyautogui.press('enter')

    # Click button to sell
    pyautogui.click(sell_x, sell_y)

    # Click first item to sell
    pyautogui.click(center_to_sell_x, center_to_sell_y)

    # Click Last pixel on slide
    pyautogui.click(max_x, max_y)

    # Click ok
    pyautogui.click(ok_x, ok_y)

