import time

import pyautogui

from config import Config
from coord import Coord
from imagesearch import imagesearcharea


class Player:
    __fought = bool
    __capacity = int
    __position = Coord
    __last_position = Coord

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

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
        self.position = Coord([-1, -1])
        self.last_position = Coord([-1, -1])

    def __str__(self):
        return "(position) \n" + str(self.position) + '\n' \
               + "(up) \n" + str(Config.up) + '\n' \
               + "(down) \n" + str(Config.down) + '\n' \
               + "(left) \n" + str(Config.left) + '\n' \
               + "(right) \n" + str(Config.right) + '\n' \
               + "(last position) \n" + str(self.last_position) + '\n' \
               + "(capacity) \n" + str(self.capacity) + '\n'

    def is_fighting(self):
        if pyautogui.pixelMatchesColor(Config.battle_list.x, Config.battle_list.y, Config.red, ) or \
                pyautogui.pixelMatchesColor(Config.battle_list.x, Config.battle_list.y, Config.pink, ):
            self.fought = True

            self.follow(Config.follow, Config.green_follow)
            return True
        else:
            self.fight()
            return False

    def fight(self):
        if not pyautogui.pixelMatchesColor(Config.monster.x, Config.monster.y, Config.gray) and self.fought:
            pyautogui.click(Config.monster.x, Config.monster.y)
            pyautogui.moveTo(5, 5)
            self.follow(Config.follow, Config.green_follow)

    def is_in_mark_center(self):
        if self.position.x < Config.left or self.position.x > Config.right \
                or self.position.y < Config.up or self.position.y > Config.down:
            if self.position == self.last_position:
                Config.mark.x, Config.mark.y = imagesearcharea(Config.markers[Config.starter_mark], Config.map_begin.x,
                                                               Config.map_begin.y, Config.map_end.x, Config.map_end.y)

            self.position.x = Config.map_begin.x + Config.mark.x + 3
            self.position.y = Config.map_begin.y + Config.mark.y + 3

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
