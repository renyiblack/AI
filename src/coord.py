class Coord:
    x = int
    y = int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + '\n' \
               + "y: " + str(self.y) + '\n'
