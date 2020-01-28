from config import Config
from player import Player


class Tibia:
    __player = Player
    __running = bool

    def __init__(self):
        self.__player = Player()
        self.__running = True

    def __str__(self):
        return "(running)" + '\n' + str(self.__running) + '\n' \
               + "(starter mark)" + '\n' + str(Config.starter_mark) + '\n' \
               + "(max markers)" + '\n' + str(Config.max_markers) + '\n' \
               + "(current mark)" + '\n' + str(Config.mark) + '\n' \
               + "(char) \n" + str(self.player) + '\n' \
               + "(map begin) \n" + str(Config.map_begin.pair) + '\n' \
               + "(map end) \n" + str(Config.map_end.pair) + '\n' \
               + "(heal) \n" + str(Config.heal) + '\n' \
               + "(follow) \n" + str(Config.follow) + '\n' \
               + "(battle list) \n" + str(Config.battle_list) + '\n'

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, boolean):
        self.__running = boolean

    @property
    def player(self):
        return self.__player
