import pyautogui

from player import Player
from coord import Coord


class Tibia:
    __map_begin = Coord
    __map_end = Coord
    __battle_list = Coord
    __follow = Coord
    __heal = Coord
    __player = Player

    __red = (255, 0, 0)  # Red battle list when we're in battle
    __pink = (255, 128, 128)  # Pink battle list when we're in battle
    __gray = (75, 75, 75)  # Gray battle list in the beginning of monster hp bar
    __black = (255, 255, 255)  # Black battle list when monster hits us
    __green_follow = (104, 246, 104)  # Green color, head, left pixel
    __exura_blue = (63, 108, 154)  # Blue color of exura ico in middle
    __white_cap = (192, 192, 192)  # White color of 0 cap in skills tab

    def __init__(self):
        self.__map_begin = Coord(1752, 27)
        self.__map_end = Coord(1859, 137)
        self.__battle_list = Coord(1748, 480)
        self.__follow = Coord(1904, 170)
        self.__heal = Coord(459, 899)
        self.__player = Player()

    def __str__(self):
        return "(map begin) \n" + str(self.__map_begin) + '\n' \
               + "(map end) \n" + str(self.__map_end) + '\n' \
               + "(char) \n" + str(self.__player) + '\n' \
               + "(heal) \n" + str(self.__heal) + '\n' \
               + "(follow) \n" + str(self.__follow) + '\n' \
               + "(battle list) \n" + str(self.__battle_list) + '\n'

    def set_player_pos(self, pos):
        self.__player.pos = pos

    def is_in_battle(self):
        return self.__player.is_fighting(self.__battle_list, self.__red, self.__pink, self.__follow,
                                         self.__green_follow)

    def are_there_monster(self):

        if not self.__player.is_fighting(self.__battle_list, self.__red, self.__pink, self.__follow,
                                         self.__green_follow) and \
                not pyautogui.pixelMatchesColor(self.__battle_list.x, self.__battle_list.y, self.__gray):

            self.__player.set_fighting(self.__battle_list, self.__follow, self.__green_follow)
            return True
        else:
            return False
