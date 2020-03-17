from config import Config
from coord import Coord
from character import Player


class Tibia:
    __player = Player
    __running = bool
    __mark = Coord
    __starter_mark = int
    __max_markers = int

    def __init__(self):
        self.__player = Player()
        self.__mark = Coord([-1, -1])
        self.__starter_mark = Config.starter_mark
        self.__max_markers = Config.max_markers
        self.__running = True

    def __str__(self):
        return "(running)" + '\n' + str(self.__running) + '\n' \
               + "(starter mark)" + '\n' + str(self.starter_mark) + '\n' \
               + "(max markers)" + '\n' + str(self.max_markers) + '\n' \
               + "(current mark)" + '\n' + str(self.mark) + '\n' \
               + "(char) \n" + str(self.player) + '\n' \
               + "(map begin) \n" + str(Config.map_begin.pair) + '\n' \
               + "(map end) \n" + str(Config.map_end.pair) + '\n' \
               + "(heal) \n" + str(Config.heal) + '\n' \
               + "(follow) \n" + str(Config.follow) + '\n' \
               + "(battle list) \n" + str(Config.battle_list) + '\n'

    @property
    def starter_mark(self):
        return self.__starter_mark

    @starter_mark.setter
    def starter_mark(self, mark):
        self.__starter_mark = mark

    @property
    def max_markers(self):
        return self.__max_markers

    @property
    def mark(self):
        return self.__mark

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, boolean):
        self.__running = boolean

    @property
    def player(self):
        return self.__player

    def player_is_in_mark_center(self):
        return self.player.is_in_mark_center(self.mark, self.starter_mark)
