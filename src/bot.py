from coord import Coord
from tibia import Tibia


class Bot:
    __running = bool
    __tibia = Tibia
    __starter_mark = int
    __max_markers = int
    __mark = Coord

    markers = ['../imgs/Markers/imagem1.png', '../imgs/Markers/imagem2.png', '../imgs/Markers/imagem3.png',
               '../imgs/Markers/imagem4.png', '../imgs/Markers/imagem5.png', '../imgs/Markers/imagem6.png',
               '../imgs/Markers/imagem7.png', '../imgs/Markers/imagem8.png', '../imgs/Markers/imagem9.png',
               '../imgs/Markers/imagem10.png', '../imgs/Markers/imagem11.png', '../imgs/Markers/imagem12.png',
               '../imgs/Markers/imagem13.png', '../imgs/Markers/imagem14.png', '../imgs/Markers/imagem15.png',
               '../imgs/Markers/imagem16.png', '../imgs/Markers/imagem17.png', '../imgs/Markers/imagem18.png',
               '../imgs/Markers/imagem19.png', '../imgs/Markers/imagem20.png']

    def __init__(self, starter_mark, max_markers):
        self.__running = True
        self.__tibia = Tibia()
        self.__starter_mark = starter_mark
        self.__max_markers = max_markers
        self.__mark = Coord(None, None)

    def __str__(self):
        return str(self.__running) + '\n' \
               + str(self.__tibia) + '\n' \
               + str(self.__starter_mark) + '\n' \
               + str(self.__max_markers) + '\n' \
               + str(self.__mark) + '\n'

    @property
    def finish(self):
        self.__running = False

    def set_char_pos(self, pos):
        self.__tibia.set_player_pos(pos)

    @property
    def is_running(self):
        return self.__running
