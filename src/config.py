import pywinauto
import pyautogui
import keyboard
import time
import re
import imagesearch


time.sleep(0.5)

'''
    Pyautogui config
    starter_mark: Starter mark
    max_markers: Max markers
'''
pyautogui.PAUSE = 0.03
pyautogui.FAILSAFE = False

print("----- Initializing markers -----")

starter_mark = 0
max_markers = 3

print("----- Loading markers -----")
print("Loading markers from ../img/markers/")

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

print("----- Getting resolution -----")

resolution = (pyautogui.size()[0] - 1, pyautogui.size()[1] - 1)
print(f"screen resolution: {resolution}")

print("----- Loading image references -----")

'''
    Images locations
'''
battle_list_header_img = '../img/battle_list/battle_list_header.png'
print(f"Loading battle list headar reference from {battle_list_header_img}")

battle_line_red_img = '../img/battle_list/battle_line_red.png'
print(f"Loading red battle line reference from {battle_line_red_img}")

battle_line_pink_img = '../img/battle_list/battle_line_pink.png'
print(f"Loading pink battle line reference from {battle_line_pink_img}")

battle_list_button_img = '../img/battle_list/button_down.png'
print(f"Loading battle list button reference from {battle_list_button_img}")

map_reference_img = '../img/map/map_reference.png'
print(f"Loading map reference from {map_reference_img}")

follow_toggled_img = '../img/follow/follow_toggled.png'
print(f"Loading follow toggled reference from {follow_toggled_img}")

follow_untoggled_img = '../img/follow/follow_untoggled.png'
print(f"Loading follow untoggled reference from {follow_untoggled_img}")

mana_img = '../img/health_mana/mana.png'
print(f"Loading mana reference from {mana_img}")

health_mana_img = '../img/health_mana/health_mana.png'
print(f"Loading health and mana reference from {health_mana_img}")

battle_list_img = '../img/battle_list/battle_list.png'
print(f"Loading battle list reference from {battle_list_img}")

print("----- Colors -----")

'''
    Colors
    
    life: Life color in 4th bar from bottom to top in status bar
    mana: Mana color in 4th bar from bottom to top in status bar
    green_follow: Green color on follow head at the top right corner
'''
life = (241, 97, 97)
print(f"Life: {life}")
mana = (101, 98, 240)
print(f"Mana: {mana}")
green_follow = (104, 246, 104)
print(f"Follow: {green_follow}")
gray_bellow_monster_hp = (64, 64, 64)
print(f"gray bellow monster hp: {gray_bellow_monster_hp}")
red_fighting = (255, 0, 0)
print(f"red fighting: {red_fighting}")
pink_fighting = (255, 128, 128)
print(f"pink fighting: {pink_fighting}")
print(f"red fighting: {red_fighting}")
black_fighting = (0, 0, 0)
print(f"black fighting: {black_fighting}")

print("----- Calculating battle list position -----")

'''
    battle_list_begin: Top left pixel inside battle list
    battle_list_end: Botton right pixel inside battle list
    battle_list_monster: Upper left corner of first monster life bar inside battle list
'''
x, y = imagesearch.imagesearch(battle_list_header_img)

battle_list_begin = (x+4, y+15)
battle_list_monster = (battle_list_begin[0]+22, battle_list_begin[1]+15)

x, y = imagesearch.imagesearcharea(battle_list_button_img, battle_list_begin[0], battle_list_begin[1], resolution[0], resolution[1])

x += battle_list_begin[0]
y += battle_list_begin[1]

battle_list_end = (x - 1, y - 9)

battle_list_monster_offset = 22

print(f"battle list begin: {battle_list_begin}")
print(f"battle list end: {battle_list_end}")
print(f"battle list monster: {battle_list_monster}")

print("----- Calculating map and follow position -----")

'''
    map_begin: Upper left corner inside map
    map_end: Botton right corner inside map
    heal: Upper middle coord of heal hotkey
    follow: Upper left coord inside head
'''
x, y = imagesearch.imagesearch(map_reference_img)

map_begin = (x - 117, y - 90)
map_end = (x - 12, y + 18)
map_center = ((map_end[0] - map_begin[0])/2 + map_begin[0],
              (map_end[1] - map_begin[1])/2 + map_begin[1])

x, y = imagesearch.imagesearch(follow_toggled_img)

if x == -1:
    x, y = imagesearch.imagesearch(follow_untoggled_img)

follow = (x + 12, y + 5)
heal = (458, 898)  # TODO REDO, it's wrong

print(f"map begin: {map_begin}")
print(f"map end: {map_end}")
print(f"map center: {map_center}")
print(f"follow: {follow}")

print("----- Calculating player map offset -----")

'''
    up: 1 pixel above center of white cross on map
    down: 1 pixel bellow center of white cross on map
    left: 1 pixel to the left of center of white cross on map
    right: 1 pixel to the right of center of white cross on map
'''
map_center_up = map_begin[1] + 53
map_center_down = map_begin[1] + 55
map_center_left = map_begin[0] + 52
map_center_right = map_begin[0] + 54

print(f"above map center: {map_center_up}")
print(f"bellow map center: {map_center_down}")
print(f"left of map center: {map_center_left}")
print(f"right of map center: {map_center_right}")

print("----- Calculating sqms around player -----")

'''
    Sqms around character
'''
x, y = imagesearch.imagesearch(mana_img)

left_player = (x - 50, y + 62)
right_player = (x + 108, y + 62)
up_player = (x + 31, y - 15)
down_player = (x + 31, y + 131)

print(f"left player: {left_player}")
print(f"right player: {right_player}")
print(f"up player: {up_player}")
print(f"down player: {down_player}")

print("----- Calculating life and mana position -----")

'''
    life_bar_low: Close to death
    life_bar_high: Quite safe
    mana_bar: When to drink

    4th line from bottom to top
'''
x, y = imagesearch.imagesearch(health_mana_img)

life_bar_low = (x + 23, y + 6)
life_bar_high = (x + 97, y + 6)
mana_bar = (x + 23, y + 19)


print(f"life bar low: {life_bar_low}")
print(f"life bar high: {life_bar_high}")
print(f"mana bar: {mana_bar}")

print("----- Connecting to application -----")

tibia = pywinauto.Application().connect(path='Xming')
tibia_dialogs = tibia.windows()
xming = re.split(r"'", str(tibia_dialogs[0]))

print(f"tibia: {tibia}")
print(f"tibia dialogs: {tibia_dialogs}")
print(f"xming: {xming}")
