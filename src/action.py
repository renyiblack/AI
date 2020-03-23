import threading
import config
import imagesearch
import pyautogui
import time


class Action(threading.Thread):
    def __init__(self):
        super().__init__()
        # Variable to store if we fought last turn or not
        self.fought = False

    def run(self):
        while(True):
            # Are we fighting?
            if self.is_fighting():
                self.fought = True
            elif self.do_we_fight():
                self.click(config.monster)
            else:
                # Did we fight?
                if self.fought:
                    # Yes, loot
                    self.loot()
                else:
                    # No, did we reach end of the path?
                    if config.starter_mark == config.max_markers:
                        # Yes, reset
                        config.starter_mark = 0
                    else:
                        # No, move
                        self.move()

            # Check if we are following
            self.follow()

    def click(self, coord):
        pyautogui.moveTo(coord)
        pyautogui.click()
        pyautogui.moveTo(5, 5)
        time.sleep(0.1)

    def is_fighting(self):
        # Is player in combat?
        if pyautogui.pixelMatchesColor(config.battle_list[0], config.battle_list[1], config.red) or \
                pyautogui.pixelMatchesColor(config.battle_list[0], config.battle_list[1], config.pink):
            print("FIGHTING!")
            return True
        else:
            print("NOT FIGHTING!")
            return False

    def do_we_fight(self):
        # Is battle list empty?
        if pyautogui.pixelMatchesColor(config.monster[0], config.monster[1], config.gray):
            # Don't fight!
            print("BATTLE EMPTY!")
            return False
        # Battle list is NOT empty! Did we fight before?
        elif self.fought:
            # Don't fight, for now
            print("FOUGHT!")
            return False
        else:
            # FIGHT MA BROTHA
            print("FIGHT!")
            return True

    def move(self):
        # Find mark on tibia minimap
        mark = imagesearch.imagesearcharea(
            config.markers[config.starter_mark], config.map_begin[0], config.map_begin[1], config.map_end[0], config.map_end[1])

        # Adjust x and y to correct positions
        x = (config.map_begin[0] + mark[0] + 3)
        y = (config.map_begin[1] + mark[1] + 3)

        # Reassign mark to the correct x, y
        mark = (x, y)

        # Is player in mark center?
        if mark[0] > config.left - 2 and mark[0] < config.right + 2 \
                and mark[1] > config.up - 2 and mark[1] < config.down + 2:
            # Yes, go to next mark
            config.starter_mark = config.starter_mark + 1
        else:
            # No, click on mark
            self.click(mark)

    def loot(self):
        print("LOOT!")
        # We didn't fight this turn, we RICH BABY
        self.fought = False


        # Time to low level player get closer to mob dead body
        time.sleep(0.5)
        '''
            Loot patern is:
                down, left, up, up, right, right, down, down
        '''
        config.tibia[config.xming[1]].type_keys('{VK_SHIFT down}')

        pyautogui.moveTo(config.down_player)
        pyautogui.click(
            button='right', x=config.down_player[0], y=config.down_player[1])
        pyautogui.click(
            button='right', x=config.diag_down_left_player[0], y=config.diag_down_left_player[1])
        pyautogui.click(
            button='right', x=config.left_player[0], y=config.left_player[1])
        pyautogui.click(
            button='right', x=config.diag_up_left_player[0], y=config.diag_up_left_player[1])
        pyautogui.click(
            button='right', x=config.up_player[0], y=config.up_player[1])
        pyautogui.click(
            button='right', x=config.diag_up_right_player[0], y=config.diag_up_right_player[1])
        pyautogui.click(
            button='right', x=config.right_player[0], y=config.right_player[1])
        pyautogui.click(
            button='right', x=config.diag_down_right_player[0], y=config.diag_down_right_player[1])

        config.tibia[config.xming[1]].type_keys('{VK_SHIFT up}')

        pyautogui.moveTo(5, 5)

    def follow(self):
        # Are we not following?
        if not pyautogui.pixelMatchesColor(config.follow[0], config.follow[1], config.green_follow):
            # FOLLOW!
            pyautogui.click(x=config.follow[0], y=config.follow[1])
            pyautogui.moveTo(5, 5)
