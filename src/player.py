import pyautogui
import time
import config
import imagesearch


def is_fighting():
    # Is player in combat?
    if pyautogui.pixelMatchesColor(config.battle_list[0], config.battle_list[1], config.red) or \
            pyautogui.pixelMatchesColor(config.battle_list[0], config.battle_list[1], config.pink):
        print("FIGHTING!")
        return True
    else:
        print("NOT FIGHTING!")
        return False


def do_we_fight(fought):
    # Is battle list empty?
    if pyautogui.pixelMatchesColor(config.monster[0], config.monster[1], config.gray):
        # Don't fight!
        print("BATTLE EMPTY!")
        return False
    # Battle list is NOT empty! Did we fight before?
    elif fought:
        # Don't fight, for now
        print("FOUGHT!")
        return False
    else:
        # FIGHT MA BROTHA
        print("FIGHT!")
        return True


def move(coord, count_trapado):
    # Find mark on tibia minimap
    mark = imagesearch.imagesearcharea(
        config.markers[config.starter_mark], config.map_begin[0], config.map_begin[1], config.map_end[0], config.map_end[1])

    # Adjust x and y to correct positions
    x = (config.map_begin[0] + mark[0] + 3)
    y = (config.map_begin[1] + mark[1] + 3)

    # Reassign mark to the correct x, y
    mark = (x, y)

    # Are we on the same spot?
    if(coord == mark):
        count_trapado += 1
        # If we are for more than N ticks, try to move manually
        if count_trapado >= 5:
            if config.map_center[0] > coord[0]:
                config.tibia[config.xming[1]].type_keys('{VK_LEFT}')
            elif config.map_center[0] < coord[0]:
                config.tibia[config.xming[1]].type_keys('{VK_RIGHT}')
            if config.map_center[1] > coord[1]:
                config.tibia[config.xming[1]].type_keys('{VK_UP}')
            elif config.map_center[1] < coord[1]:
                config.tibia[config.xming[1]].type_keys('{VK_DOWN}')
        # Not trapped, just click normally
        else:
            click('left', mark)

        return mark, count_trapado

    # Is player on mark center?
    elif mark[0] > config.left - 3 and mark[0] < config.right + 3 \
            and mark[1] > config.up - 3 and mark[1] < config.down + 3:
        # Yes, go to next mark
        config.starter_mark += 1
        count_trapado = 0

        return mark, count_trapado
    else:
        # No, reset counter
        count_trapado = 0

        return mark, count_trapado


def loot():
    print("LOOT!")

    # Time to low level player get closer to mob dead body
    time.sleep(0.5)
    '''
        Loot patern is: down, left, up, up, right, right, down, down
    '''
    config.tibia[config.xming[1]].type_keys('{VK_SHIFT down}')

    click('right', config.down_player)
    click('right', config.diag_down_left_player)
    click('right', config.left_player)
    click('right', config.diag_up_left_player)
    click('right', config.up_player)
    click('right', config.diag_up_right_player)
    click('right', config.right_player)
    click('right', config.diag_down_right_player)

    config.tibia[config.xming[1]].type_keys('{VK_SHIFT up}')


def follow():
    # If follow is not green
    if not pyautogui.pixelMatchesColor(config.follow[0], config.follow[1], config.green_follow):
        # FOLLOW!
        pyautogui.click(x=config.follow[0], y=config.follow[1])


def click(bu, coords):
    pyautogui.moveTo(x=coords[0], y=coords[1])
    pyautogui.click(button=bu)
