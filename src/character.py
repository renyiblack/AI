import time

import pyautogui

import config
import imagesearch
import pywinauto


class Character:
    __fought = bool
    __capacity = int

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def fought(self):
        return self.__fought

    # TODO spells

    def __init__(self):
        self.__fought = False
        self.capacity = 999

    def __str__(self):
        return "(fought) \n{fought}\n" \
               + "(capacity) \n{capacity}\n"

    def is_fighting(self, tibia, dialogs):
        if pyautogui.pixelMatchesColor(config.battle_list[0], config.battle_list[1], config.red) or \
                pyautogui.pixelMatchesColor(config.battle_list[0], config.battle_list[1], config.pink):

            self.__fought = True
            self.follow(config.follow, config.green_follow, tibia, dialogs)
            return True
        elif not pyautogui.pixelMatchesColor(config.monster[0],
                                             config.monster[1],
                                             config.gray) and not self.fought:

            print("to indo bater coroi")
            tibia[dialogs[0]].click(coords=(config.monster[0],
                                            config.monster[1]))
            time.sleep(0.05)
            pyautogui.moveTo(0, 0)
            self.follow(config.follow, config.green_follow, tibia, dialogs)
            return False

    def is_in_mark_center(self, starter_mark, tibia, dialogs):

        mark = imagesearch.imagesearcharea(
            config.markers[starter_mark], config.map_begin[0],
            config.map_begin[1], config.map_end[0], config.map_end[1])

        x = (config.map_begin[0] + mark[0] + 3)
        y = (config.map_begin[1] + mark[1] + 3)

        mark = (x, y)

        print(f"mark - {mark}")
        print(f"left - {config.left}")
        print(f"right - {config.right}")
        print(f"up - {config.up}")
        print(f"down - {config.down}")

        if mark[0] > config.left - 2 and mark[0] < config.right + 2 \
                and mark[1] > config.up - 2 and mark[1] < config.down + 2:
            print("yo")
            return True
        else:
            tibia[dialogs[0]].click(coords=(mark[0], mark[1]))
            pyautogui.moveTo(5, 5)
            return False

    def loot(self, tibia, dialogs, obs):
        self.__fought = False

        time.sleep(0.7)

        print("looteando")

        tibia[dialogs[0]].maximize()
        time.sleep(0.05)
        pyautogui.keyDown('shift')
        pyautogui.click(button='right', x=config.down_player[0],
                        y=config.down_player[1])
        pyautogui.click(button='right',
                        x=config.diag_down_left_player[0],
                        y=config.diag_down_left_player[1])
        pyautogui.click(button='right',
                        x=config.left_player[0],
                        y=config.left_player[1])
        pyautogui.click(button='right',
                        x=config.diag_up_left_player[0],
                        y=config.diag_up_left_player[1])
        pyautogui.click(button='right',
                        x=config.up_player[0],
                        y=config.up_player[1])
        pyautogui.click(button='right',
                        x=config.diag_up_right_player[0],
                        y=config.diag_down_right_player[1])
        pyautogui.click(button='right',
                        x=config.right_player[0],
                        y=config.right_player[1])
        pyautogui.click(button='right',
                        x=config.diag_down_right_player[0],
                        y=config.diag_down_right_player[1])
        pyautogui.keyUp('shift')
        obs.WindowedProjector.minimize()
        obs.WindowedProjector.maximize()
        time.sleep(0.2)

        pyautogui.moveTo(5, 5)

    @staticmethod
    def follow(follow, green_follow, tibia, dialogs):
        if not pyautogui.pixelMatchesColor(follow[0], follow[1], green_follow):
            tibia[dialogs[0]].click(coords=(follow[0], follow[1]))
            pyautogui.moveTo(5, 5)
