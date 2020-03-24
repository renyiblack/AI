import pywinauto
import pyautogui
import keyboard
import time
import re
import imagesearch

'''
    markers: path to images used as markers for the bot movement
'''
markers = [
    '../img/markers/marker1.png', '../img/markers/marker2.png',
    '../img/markers/marker3.png', '../img/markers/marker4.png',
    '../img/markers/marker5.png', '../img/markers/marker6.png',
    '../img/markers/marker7.png', '../img/markers/marker8.png',
    '../img/markers/marker9.png', '../img/markers/marker10.png',
    '../img/markers/marker11.png', '../img/markers/marker12.png',
    '../img/markers/marker13.png', '../img/markers/marker14.png',
    '../img/markers/marker15.png', '../img/markers/marker16.png',
    '../img/markers/marker17.png', '../img/markers/marker18.png',
    '../img/markers/marker19.png', '../img/markers/marker20.png'
]

'''
    hunt: hunt location
'''
hunt = "hunt"

'''
    Pyautogui config
    starter_mark: Starter mark
    max_markers: Max markers
'''
pyautogui.PAUSE = 0.0005
pyautogui.FAILSAFE = False

pyautogui.moveTo(x=5, y=5)

starter_mark = 0
max_markers = 3

'''
    Colors

    red: Red battle list when we're in battle
    pink: Pink battle list when we're in battle
    gray: Gray battle list in the beginning of monster hp bar
    green_follow: Green color, head, left pixel
    blue_heal: Blue color of heal in middle right before resetting
    white_cap: White color of cap in skills tab
    life: Life color in 4 bar
    mana: Mana color in 4 bar
'''
red = (255, 0, 0)
pink = (255, 128, 128)
gray = (64, 64, 64)
green_follow = (104, 246, 104)
blue_heal = (63, 108, 154)
white_cap = (192, 192, 192)
life = (241, 97, 97)
mana = (101, 98, 240)

'''
    map_begin: Upper left corner inside map
    map_end: Botton right corner inside map
    battle_list: Upper left corner inside battle list
    monster: Upper left corner of monster life bar inside battle list
    heal: Upper middle coord of heal hotkey
    follow: Upper left coord inside head
'''
x, y = imagesearch.imagesearch("../img/map/map.png")
map_begin = (x - 118, y - 18)
map_end = (x - 13, y + 90)

x, y = imagesearch.imagesearch("../img/battle_list/battle_list.png")
battle_list = (x + 4, y + 15)
monster = (x + 26, y + 30)

x, y = imagesearch.imagesearch("../img/follow/follow.png")
follow = (x + 12, y + 5)
heal = (458, 898)  # REDO, it's wrong

'''
    up: 1 pixel above center of white cross on map
    down: 1 pixel bellow center of white cross on map
    left: 1 pixel to the left of center of white cross on map
    right: 1 pixel to the right of center of white cross on map
'''
up = map_begin[1] + 53
down = map_begin[1] + 55
left = map_begin[0] + 52
right = map_begin[0] + 54


'''
    Sqms around character
'''
x, y = imagesearch.imagesearch("../img/character/character_mana.png")

left_player = (x - 50, y + 62)
right_player = (x + 108, y + 62)
up_player = (x + 31, y - 15)
down_player = (x + 31, y + 131)
diag_up_left_player = (x - 50, y - 15)
diag_up_right_player = (x + 108, y - 15)
diag_down_left_player = (x - 50, y + 131)
diag_down_right_player = (x + 108, y + 131)

'''
    life_bar_low: Close to death
    life_bar_high: Quite safe
    mana_bar: When to drink

    4th line from bottom to top
'''
x, y = imagesearch.imagesearch("../img/status/status.png")

life_bar_low = (x + 23, y + 7)
life_bar_high = (x + 88, y + 7)
mana_bar = (x + 23, y + 20)

tibia = pywinauto.Application().connect(path='Xming')
tibia_dialogs = tibia.windows()
xming = re.split(r"'", str(tibia_dialogs[0]))
