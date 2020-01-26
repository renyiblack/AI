class Coord:
    __x = int
    __y = int

    def __init__(self, pair):
        self.pair = pair

    def __str__(self):
        return "pair: " + str(self.__x) + ", " + str(self.__y) + '\n'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def pair(self):
        return self.__x, self.__y

    @pair.setter
    def pair(self, pair):
        try:
            self.__x, self.__y = pair
        except ValueError:
            raise ValueError("Pass an iterable with two items")
