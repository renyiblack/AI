import config
import player
import threading
import time
import pyautogui
import imagesearch


class Player(threading.Thread):
    def __init__(self):
        super(Player, self).__init__()
        # If we fought or not last turn
        self.fought = False
        # Current mark
        self.current_mark = (-1, -1)
        # Last mark coord
        self.last_mark = (-1, -1)
        # Number of iterations we didn't move
        self.count_trapped = 0

    def run(self):
        while(True):
            if self.is_fighting():
                # print(">>> fighting")
                self.fought = True
                follow()
            elif self.should_fight_back():
                # print(">>> being hit")
                self.fought = True
                follow()
            elif self.should_fight_anyone():
                # print(">>> hit anyone")
                click('left', config.battle_list_monster)
                self.fought = True
                follow()
            else:
                if self.fought:
                    # print(">>> loot")
                    loot()
                    self.fought = False
                else:
                    # print(">>> move")
                    self.move()

    def is_fighting(self):
        x = config.battle_list_begin[0]

        # Find any red or pink pixel inside battle list
        for offset in range(config.battle_list_begin[1], config.battle_list_end[1] + config.battle_list_monster_offset, config.battle_list_monster_offset):
            y = offset
            # is pixel red?
            if pyautogui.pixelMatchesColor(x, y, config.red_fighting):
                # print(f">>> is fighting with: {(x, y)}")
                return True
            # is pixel pink?
            elif pyautogui.pixelMatchesColor(x, y, config.pink_fighting):
                # print(f">>> is fighting with: {(x, y)}")
                return True

    def should_fight_back(self):
        x = config.battle_list_begin[0]

        for offset in range(config.battle_list_begin[1], config.battle_list_end[1] + config.battle_list_monster_offset, config.battle_list_monster_offset):
            y = offset - 15
            # is pixel black?
            if pyautogui.pixelMatchesColor(x, y, config.black_fighting):
                # print(f">>> hit back if not fought mob at: {(x, y)}")
                click('left', (x, y))
                return not self.fought
        return False

    def should_fight_anyone(self):
        if pyautogui.pixelMatchesColor(config.battle_list_monster[0], config.battle_list_monster[1], config.gray_bellow_monster_hp):
            # print(">>> battle list empty")
            return False
        else:
            # print(">>> battle list not empty")
            return not self.fought

    def move(self):
        self.find_mark()

        if self.is_trapped():
            # print(">>> increasing trapped counter")
            self.count_trapped += 1

        elif self.is_on_mark():
            # print(">>> moving to next mark")
            if config.starter_mark + 1 == config.max_markers:
                # print(">>> reseting marks")
                config.starter_mark = 0
            else:
                config.starter_mark += 1
                self.count_trapped = 0
                self.find_mark()
                click('left', self.current_mark)
        else:
            if(self.last_mark != self.current_mark):
                click('left', self.current_mark)

    def find_mark(self):
        # print(">>> looking for mark on map")
        mark = imagesearch.imagesearcharea(config.markers[config.starter_mark], config.map_begin[0], config.map_begin[1], config.map_end[0], config.map_end[1])

        if mark[0] == -1:
            # print(">>> mark not found, try next one")
            config.starter_mark += 1
            self.current_mark = self.last_mark

        mark = (config.map_begin[0] + mark[0] + 3,
                      (config.map_begin[1] + mark[1] + 3))

        # print(f">>> mark found at: {mark}")

        self.current_mark = mark

    def is_trapped(self):
        if(self.last_mark == self.current_mark):
            # After N ticks, try to move manually
            if self.count_trapped >= 10:
                # print(">>> trapped! trying to move manualy")
                if config.map_center[0] > self.last_mark[0]:
                    config.tibia[config.xming[1]].type_keys('{VK_LEFT}')
                elif config.map_center[0] < self.last_mark[0]:
                    config.tibia[config.xming[1]].type_keys('{VK_RIGHT}')
                if config.map_center[1] > self.last_mark[1]:
                    config.tibia[config.xming[1]].type_keys('{VK_UP}')
                elif config.map_center[1] < self.last_mark[1]:
                    config.tibia[config.xming[1]].type_keys('{VK_DOWN}')
                return True
            else:
                # print(">>> maybe trapped?")
                click('left', self.current_mark)
                return False
        else:
            # print(">>> not trapped")
            return False

    def is_on_mark(self):
        offset = 3
        # Is player on mark center?
        if self.current_mark[0] > config.map_center_left - offset and self.current_mark[0] < config.map_center_right + offset \
                and self.current_mark[1] > config.map_center_up - offset and self.current_mark[1] < config.map_center_down + offset:
            # print(">>> we are inside the mark")
            return True
        else:
            # print(">>> we are not inside the mark")
            return False


def loot():
    # Time to low level player get closer to mob dead body
    # time.sleep(0.3)
    '''
        Loot patern is: down, left, up, up, right, right, down, down
    '''
    config.tibia[config.xming[1]].type_keys('{VK_SHIFT down}')

    click('right', config.down_player)
    click('right', (config.left_player[0], config.down_player[1]))
    click('right', config.left_player)
    click('right', (config.left_player[0], config.up_player[1]))
    click('right', config.up_player)
    click('right', (config.right_player[0], config.up_player[1]))
    click('right', config.right_player)
    click('right', (config.right_player[0], config.down_player[1]))

    config.tibia[config.xming[1]].type_keys('{VK_SHIFT up}')


def follow():
    # If follow is not green
    if not pyautogui.pixelMatchesColor(config.follow[0], config.follow[1], config.green_follow):
        pyautogui.click(x=config.follow[0], y=config.follow[1])


def click(bu, coords):
    # print(">>> clicked")
    pyautogui.moveTo(x=coords[0], y=coords[1])
    pyautogui.click(button=bu)
