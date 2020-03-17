from coord import Coord

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


class Config:
    markers = ['../img/markers/marker1.png', '../img/markers/marker2.png', '../img/markers/marker3.png',
               '../img/markers/marker4.png', '../img/markers/marker5.png', '../img/markers/marker6.png',
               '../img/markers/marker7.png', '../img/markers/marker8.png', '../img/markers/marker9.png',
               '../img/markers/marker10.png', '../img/markers/marker11.png', '../img/markers/marker12.png',
               '../img/markers/marker13.png', '../img/markers/marker14.png', '../img/markers/marker15.png',
               '../img/markers/marker16.png', '../img/markers/marker17.png', '../img/markers/marker18.png',
               '../img/markers/marker19.png', '../img/markers/marker20.png']
    hunt = "hunt"

    red = (255, 0, 0)
    pink = (255, 128, 128)
    gray = (64, 64, 64)
    black = (255, 255, 255)
    green_follow = (104, 246, 104)
    blue_heal = (63, 108, 154)
    white_cap = (192, 192, 192)

    map_begin = Coord([1752, 27])
    map_end = Coord([1859, 137])
    battle_list = Coord([1748, 480])
    monster = Coord([1770, 495])
    follow = Coord([1904, 170])
    heal = Coord([459, 899])  # REDO

    starter_mark = 0
    max_markers = 2
    up = 81
    down = 83
    left = 1805
    right = 1807

    left_player = Coord([890, 465])
    right_player = Coord([130, 465])
    up_player = Coord([955, 405])
    down_player = Coord([955, 535])
    diag_up_left_player = Coord([890, 405])
    diag_up_right_player = Coord([1020, 405])
    diag_down_left_player = Coord([890, 535])
    diag_down_right_player = Coord([1030, 535])

    life_bar_low = Coord([1788, 309])
    life_low = (241, 97, 97)
    life_bar_high = Coord([1852, 309])
    life_high = (241, 97, 97)
    mana_bar = Coord([1771, 322])
    mana = (101, 98, 240)
