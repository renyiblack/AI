import time

import pyautogui

from colors import Colors
from coord import Coord
from imagesearch import imagesearcharea


class Player:
    __fought = bool
    __capacity = int
    __up = int
    __down = int
    __left = int
    __right = int
    __position = Coord
    __last_position = Coord

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def up(self):
        return self.__up

    @up.setter
    def up(self, up):
        self.__up = up

    @property
    def down(self):
        return self.__down

    @down.setter
    def down(self, down):
        self.__down = down

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def last_position(self):
        return self.__last_position

    @last_position.setter
    def last_position(self, last_position):
        self.__last_position = last_position

    @property
    def fought(self):
        return self.__fought

    @fought.setter
    def fought(self, boolean):
        self.__fought = boolean

    # TODO spells

    def __init__(self):
        self.fought = False
        self.up = 81
        self.down = 83
        self.left = 1805
        self.right = 1807
        self.position = Coord([-1, -1])
        self.last_position = Coord([-1, -1])

    def __str__(self):
        return "(position) \n" + str(self.position) + '\n' \
               + "(up) \n" + str(self.up) + '\n' \
               + "(down) \n" + str(self.down) + '\n' \
               + "(left) \n" + str(self.left) + '\n' \
               + "(right) \n" + str(self.right) + '\n' \
               + "(last position) \n" + str(self.last_position) + '\n' \
               + "(capacity) \n" + str(self.capacity) + '\n'

    def is_fighting(self, battle_list, monster, follow):
        if pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, Colors.red, ) or \
                pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, Colors.pink, ):
            self.fought = True

            self.follow(follow, Colors.green_follow)
            return True
        else:
            self.fight(monster, follow)
            return False

    def fight(self, monster, follow):
        if not pyautogui.pixelMatchesColor(monster.x, monster.y, Colors.gray) and self.fought:
            pyautogui.click(monster.x, monster.y)
            pyautogui.moveTo(5, 5)
            self.follow(follow, Colors.green_follow)

    def is_in_mark_center(self, mark, map_begin, map_end, markers, starter_mark):
        if self.position.x < self.__left or self.position.x > self.position \
                or self.position.y < self.__up or self.position.y > self.__down:
            # if self.tibia.char.pos == self.tibia.char.last_pos:
            mark.x, mark.y = imagesearcharea(markers[starter_mark], map_begin.x, map_begin.y, map_end.x, map_end.y)
            self.position.x = map_begin.x + mark.x + 3
            self.position.y = map_begin.y + mark.y + 3
            pyautogui.click(self.position.x, self.position.y)
            pyautogui.moveTo(5, 5)
            return True
        else:
            pyautogui.click(self.position.x, self.position.y)
            pyautogui.moveTo(5, 5)
            return False

    @staticmethod
    def heal():
        # TODO REDO
        if not (pyautogui.pixelMatchesColor(1237, 310, (255, 113, 113))):  # life bar(status) ~30%
            pyautogui.press('f1')
            print(">>> using life pot...")
        else:
            if not (pyautogui.pixelMatchesColor(1295, 310, (255, 113, 113))):  # life bar(status) ~80%
                pyautogui.press('f3')
                print(">>> healing...")
            if not (pyautogui.pixelMatchesColor(1260, 323, (116, 113, 255))):  # mana bar(status) 30%
                pyautogui.press('f2')
                print(">>> using mana pot...")

    def loot(self):
        self.fought = False
        time.sleep(0.7)

        pyautogui.keyDown('shift')
        pyautogui.click(button='right', x=770, y=370)  # down
        pyautogui.click(button='right', x=730, y=370)  # left
        pyautogui.click(button='right', x=730, y=320)  # up
        pyautogui.click(button='right', x=730, y=290)  # up
        pyautogui.click(button='right', x=770, y=290)  # right
        pyautogui.click(button='right', x=810, y=290)  # right
        pyautogui.click(button='right', x=810, y=320)  # down
        pyautogui.click(button='right', x=810, y=370)  # down
        pyautogui.keyUp('shift')

        pyautogui.moveTo(5, 5)

    @staticmethod
    def follow(follow, green_follow):
        if not pyautogui.pixelMatchesColor(follow.x, follow.y, green_follow):
            pyautogui.click(follow.x, follow.y)
            pyautogui.moveTo(5, 5)
