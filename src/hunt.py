import os

import keyboard
import psutil
import pyautogui

from config import Config
from tibia import Tibia


def hunt():
    pyautogui.PAUSE = 0.000005
    pyautogui.FAILSAFE = False
    pyautogui.click(5, 5)

    tibia = Tibia()

    memory_debug = open("../txt/memory_debug.txt", "a+")

    while tibia.running:
        program = psutil.Process(os.getpid())

        update(tibia)
        process(tibia)
        debug(tibia)

        memory_debug.write(str(program.memory_info().rss) + "-" + str(Config.starter_mark) + "\n")


def update(tibia):
    if keyboard.is_pressed('q'):
        tibia.running = False
    else:
        # TODO ASYNC
        print(tibia)
        if not tibia.player.is_fighting():
            if tibia.player.fought:
                tibia.player.loot()
            else:
                if Config.starter_mark == Config.max_markers:
                    Config.starter_mark = 0
                else:
                    if not tibia.player.is_fighting():
                        if not tibia.player.is_in_mark_center():
                            Config.starter_mark = Config.starter_mark + 1

                    tibia.player.last_pos = tibia.player.position


def process(tibia):
    pass


def debug(tibia):
    print(tibia)
