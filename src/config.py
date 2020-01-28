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
    
    mark: Mark position on map
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
    pink = (255, 128, 128)  # Pink battle list when we're in battle
    gray = (75, 75, 75)  # Gray battle list in the beginning of monster hp bar
    black = (255, 255, 255)  # Black battle list when monster hits us
    green_follow = (104, 246, 104)  # Green color, head, left pixel
    blue_heal = (63, 108, 154)  # Blue color of heal in middle right before resetting
    white_cap = (192, 192, 192)  # White color of 0 cap in skills tab

    mark = Coord([-1, -1])
    map_begin = Coord([1198, 27])
    map_end = Coord([1305, 137])
    battle_list = Coord([1194, 456])
    monster = Coord([1194, 456])
    follow = Coord([1350, 170])
    heal = Coord([459, 587])

    starter_mark = 0
    max_markers = 2
    up = 81
    down = 83
    left = 1805
    right = 1807
