import pywinauto
import pyautogui
import keyboard
import time
'''
    markers: path to images used as markers for the bot movement
    hunt: hunt location
    
    red: Red battle list when we're in battle
    pink: Pink battle list when we're in battle
    gray: Gray battle list in the beginning of monster hp bar
    black: Black battle list when monster hits us
    green_follow: Green color, head, left pixel
    blue_heal: Blue color of heal in middle right before resetting
    white_cap: White color of cap in skills tab
    
    map_begin: Top left inside map position
    map_end: Bottom right inside map position
    battle_list: Battle list top left inside position
    monster: Monster position in battle list
    follow: Top left(head) position of follow icon
    heal: Heal position right after cool down ends
    
    starter_mark: Marker where the route starts
    max_markers: Maximum numbers of marks
    up: Pixel above white cross center on map
    down: Pixel bellow white cross center on map
    left: Pixel left of white cross center on map
    right: Pixel right of white cross center on map
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
hunt = "hunt"

pyautogui.PAUSE = 0.00005
pyautogui.moveTo(5, 5)

red = (255, 0, 0)
pink = (255, 128, 128)
gray = (64, 64, 64)
black = (255, 255, 255)
green_follow = (104, 246, 104)
blue_heal = (63, 108, 154)
white_cap = (192, 192, 192)
life_low = (241, 97, 97)
life_high = (241, 97, 97)
mana = (101, 98, 240)

map_begin = (1752, 4)
map_end = (1859, 114)
battle_list = (1748, 457)
monster = (1770, 472)
follow = (1904, 147)
heal = (458, 898)  # REDO, it's wrong

starter_mark = 0
max_markers = 2
up = 58
down = 60
left = 1804
right = 1806

left_player = (880, 486)
right_player = (1010, 486)
up_player = (960, 415)
down_player = (960, 540)
diag_up_left_player = (880, 415)
diag_up_right_player = (1010, 415)
diag_down_left_player = (880, 540)
diag_down_right_player = (1010, 540)

life_bar_low = (1776, 286)
life_bar_high = (1822, 286)
mana_bar = (1776, 299)

# Change Blacknin to your character name
tibia = pywinauto.Application().connect(title="Tibia - Blacknin")
tibia_dialogs = tibia.windows()
obs = pywinauto.Application().connect(title="Windowed Projector (Preview)")
obs.WindowedProjector.minimize()
obs.WindowedProjector.maximize()
tibia.TibiaBlacknin.minimize()
tibia.TibiaBlacknin.maximize()
