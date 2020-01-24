import pyautogui

from player import Player
from coord import Coord


class Tibia:
    __map_begin = Coord
    __map_end = Coord
    __battle_list = Coord
    __monster = Coord
    __follow = Coord
    __heal = Coord
    __mark = Coord
    __player = Player
    __red = (255, 0, 0)  # Red battle list when we're in battle
    __pink = (255, 128, 128)  # Pink battle list when we're in battle
    __gray = (75, 75, 75)  # Gray battle list in the beginning of monster hp bar
    __black = (255, 255, 255)  # Black battle list when monster hits us
    __green_follow = (104, 246, 104)  # Green color, head, left pixel
    __blue_heal = (63, 108, 154)  # Blue color of heal in middle right before resetting
    __white_cap = (192, 192, 192)  # White color of 0 cap in skills tab
    __running = bool
    __start = int
    __max = int

    def __init__(self, starter_mark, max_markers):
        self.__map_begin = Coord(1752, 27)
        self.__map_end = Coord(1859, 137)
        self.__battle_list = Coord(1748, 480)
        self.__follow = Coord(1904, 170)
        self.__heal = Coord(459, 899)
        self.__player = Player()
        self.__start = starter_mark
        self.__max = max_markers
        self.__running = True
        self.__mark = Coord(None, None)

    def __str__(self):
        return str(self.__running) + '\n' \
               + str(self.__start) + '\n' \
               + str(self.__max) + '\n' \
               + str(self.__mark) + '\n' \
               + "(map begin) \n" + str(self.__map_begin) + '\n' \
               + "(map end) \n" + str(self.__map_end) + '\n' \
               + "(char) \n" + str(self.__player) + '\n' \
               + "(heal) \n" + str(self.__heal) + '\n' \
               + "(follow) \n" + str(self.__follow) + '\n' \
               + "(battle list) \n" + str(self.__battle_list) + '\n'

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, boolean):
        self.__running = boolean

    @property
    def player(self):
        return self.__player

    def player_is_fighting(self):
        return self.player.is_fighting(self.__battle_list, self.__monster, self.__red, self.__pink, self.__gray, self.__follow, self.__green_follow)
