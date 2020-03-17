import os

import keyboard
import psutil
import pyautogui

from config import Config
from tibia import Tibia


def hunt():
    pyautogui.PAUSE = 0.1
    pyautogui.click(5, 5)

    tibia = Tibia()

    memory_debug = open("../txt/memory_debug.txt", "a+")

    while tibia.running:
        program = psutil.Process(os.getpid())

        run(tibia)
        debug(tibia)

        memory_debug.write(str(program.memory_info().rss) + "-" + str(Config.starter_mark) + "\n")


def run(tibia):
    if keyboard.is_pressed('q'):
        tibia.running = False
    else:
        # TODO ASYNC
        if not tibia.player.is_fighting():
            if tibia.player.fought:
                tibia.player.loot()
            else:
                if tibia.starter_mark == tibia.max_markers:
                    tibia.starter_mark = 0
                elif tibia.player_is_in_mark_center():
                    tibia.starter_mark = tibia.starter_mark + 1

                tibia.player.last_position = tibia.player.position


def debug(tibia):
    print(tibia)
