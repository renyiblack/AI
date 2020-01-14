import pyautogui

from coord import Coord
from imagesearch import imagesearcharea


class Player:
    __capacity = int
    __click_up = int
    __click_down = int
    __click_left = int
    __click_right = int

    __attacking = bool
    __screenshot = None

    __pos = Coord
    __last_pos = Coord

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    # TODO spells

    def __init__(self):
        self.__click_up = 81
        self.__click_down = 83
        self.__click_left = 1805
        self.__click_right = 1807
        self.__pos = Coord(None, None)
        self.__last_pos = Coord(None, None)

    def __str__(self):
        return "(pos) \n" + str(self.__pos) + '\n' \
               + "(up) \n" + str(self.__click_up) + '\n' \
               + "(down) \n" + str(self.__click_down) + '\n' \
               + "(left) \n" + str(self.__click_left) + '\n' \
               + "(right) \n" + str(self.__click_right) + '\n' \
               + "(attacking) \n" + str(self.__attacking) + '\n' \
               + "(last pos) \n" + str(self.__last_pos) + '\n' \
               + "(capacity) \n" + str(self.__capacity) + '\n'

    def is_fighting(self, battle_list, red, pink, follow, green_follow):
        if pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, red) or \
                pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, pink):
            self.__attacking = True
            self.set_follow(follow, green_follow)
            return True
        else:
            return False

    def set_fighting(self, battle_list, follow, green_follow):
        pyautogui.click(battle_list.x, battle_list.y)
        pyautogui.moveTo(5, 5)

        self.__attacking = True
        self.set_follow(follow, green_follow)

    def are_we_in_map_center(self, mark, map_begin, map_end, markers, starter_mark):
        if self.__pos.x < self.__click_left or self.__pos.x > self.__click_right \
                or self.__pos.y < self.__click_up or self.__pos.y > self.__click_down:
            # if self.tibia.char.pos == self.tibia.char.last_pos:
            mark.x, mark.y = imagesearcharea(markers[starter_mark], map_begin.x, map_begin.y, map_end.x, map_end.y)
            self.__pos.x = map_begin.x + mark.x + 3
            self.__pos.y = map_begin.y + mark.y + 3
            pyautogui.click(self.__pos.x, self.__pos.y)
            pyautogui.moveTo(5, 5)
            return True
        else:
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

    @staticmethod
    def loot():
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
    def set_follow(follow, green_follow):
        if not pyautogui.pixelMatchesColor(follow.x, follow.y, green_follow):
            pyautogui.click(follow.x, follow.y)
            pyautogui.moveTo(5, 5)

    def set_pos(self, x, y):
        self.__pos.x = x
        self.__pos.y = y
