from coord import Coord
from player import Player


class Tibia:
    __map_begin = Coord
    __map_end = Coord
    __battle_list = Coord
    __monster = Coord
    __follow = Coord
    __heal = Coord
    __mark = Coord
    __player = Player
    __running = bool
    __start = int
    __max = int

    __markers = ['../img/markers/marker1.png', '../img/markers/marker2.png', '../img/markers/marker3.png',
                 '../img/markers/marker4.png', '../img/markers/marker5.png', '../img/markers/marker6.png',
                 '../img/markers/marker7.png', '../img/markers/marker8.png', '../img/markers/marker9.png',
                 '../img/markers/marker10.png', '../img/markers/marker11.png', '../img/markers/marker12.png',
                 '../img/markers/marker13.png', '../img/markers/marker14.png', '../img/markers/marker15.png',
                 '../img/markers/marker16.png', '../img/markers/marker17.png', '../img/markers/marker18.png',
                 '../img/markers/marker19.png', '../img/markers/marker20.png']

    def __init__(self, starter_mark, max_markers):
        self.__map_begin = Coord([1198, 27])
        self.__map_end = Coord([1305, 137])
        self.__battle_list = Coord([1194, 456])
        self.__monster = Coord([1194, 456])
        self.__follow = Coord([1350, 170])
        self.__heal = Coord([459, 587])
        self.__player = Player()
        self.__start = starter_mark
        self.__max = max_markers
        self.__running = True
        self.__mark = Coord([-1, -1])

    def __str__(self):
        return "(running)" + '\n' + str(self.__running) + '\n' \
                                                          "(starter mark)" + '\n' + str(self.__start) + '\n' \
                                                                                                        "(max markers)" + '\n' + str(
            self.__max) + '\n' \
                          "(current mark)" + '\n' + str(self.__mark) + '\n' \
               + "(map begin) \n" + str(self.__map_begin.pair) + '\n' \
               + "(map end) \n" + str(self.__map_end.pair) + '\n' \
               + "(char) \n" + str(self.__player) + '\n' \
               + "(heal) \n" + str(self.__heal) + '\n' \
               + "(follow) \n" + str(self.__follow) + '\n' \
               + "(battle list) \n" + str(self.__battle_list) + '\n'

    @property
    def map_begin(self):
        return self.__map_begin

    @property
    def map_end(self):
        return self.__map_end

    @property
    def mark(self):
        return self.__mark

    @property
    def markers(self):
        return self.__markers

    @property
    def starter_mark(self):
        return self.__start

    @starter_mark.setter
    def starter_mark(self, mark):
        self.__start = mark

    @property
    def max_markers(self):
        return self.__max

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, boolean):
        self.__running = boolean

    @property
    def player(self):
        return self.__player

    @property
    def battle_list(self):
        return self.__battle_list

    @property
    def monster(self):
        return self.__monster

    @property
    def follow(self):
        return self.__follow

    def player_is_fighting(self):
        return self.player.is_fighting(self.battle_list, self.monster, self.follow)

    def are_we_in_map_center(self):
        return self.player.are_we_in_map_center(self.mark, self.map_begin, self.map_end, self.markers, self.starter_mark)
