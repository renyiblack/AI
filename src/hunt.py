import os
import time

import keyboard
import psutil
import pyautogui

from bot import Bot
from imagesearch import imagesearcharea


def hunt(starter_mark, max_markers):
    pyautogui.PAUSE = 0.000005
    pyautogui.FAILSAFE = False
    pyautogui.click(5, 5)

    bot = Bot(starter_mark, max_markers)

    memory_debug = open("../txt/memory_debug.txt", "a+")

    while bot.is_running():
        program = psutil.Process(os.getpid())

        update(bot)
        process(bot)
        debug(bot)

        memory_debug.write(str(program.memory_info().rss) + "-" + str(starter_mark) + "\n")


def update(bot):
    if keyboard.is_pressed('q'):
        bot.finish()
    else:
        # TODO make it check cap and sell loot
        # Can we heal? make class with time.time()
        # if pyautogui.pixelMatchesColor(heal.x, heal.y, exura_blue):
        #     heal_low_lvl()

        if not bot.tibia.is_in_battle():
            if not bot.is_in_battle():
                bot.set_not_attacking()
                time.sleep(0.7)
                bot.tibia.char.loot()
            else:
                if bot.starter_mark == bot.max_markers:
                    bot.starter_mark = 0
                else:
                    # Search for mark on map, returns pos[0,0], needs to sum with original map[0,0]
                    bot.mark.x, bot.mark.y = imagesearcharea(bot.markers[bot.starter_mark],
                                                             bot.tibia.map_begin.x,
                                                             bot.tibia.map_begin.y,
                                                             bot.tibia.map_end.x,
                                                             bot.tibia.map_end.y)

                    bot.set_char_pos(bot.tibia.map_begin.x + bot.mark.x + 3, bot.tibia.map_begin.y + bot.mark.y + 3)

                    if not bot.tibia.are_there_monster():
                        if not bot.are_we_in_map_center():
                            bot.starter_mark = bot.starter_mark + 1

                    bot.tibia.char.last_pos = bot.tibia.char.pos


def process(bot):
    pass


def debug(bot):
    print(bot)
