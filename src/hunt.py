import os

import keyboard
import psutil
import pyautogui

from tibia import Tibia


def hunt(starter_mark, max_markers):
    pyautogui.PAUSE = 0.000005
    pyautogui.FAILSAFE = False
    pyautogui.click(5, 5)

    tibia = Tibia(starter_mark, max_markers)

    memory_debug = open("../txt/memory_debug.txt", "a+")

    while tibia.running:
        program = psutil.Process(os.getpid())

        update(tibia)
        process(tibia)
        debug(tibia)

        memory_debug.write(str(program.memory_info().rss) + "-" + str(starter_mark) + "\n")


def update(tibia):
    if keyboard.is_pressed('q'):
        tibia.running = False
    else:
        # TODO ASYNC
        print(tibia)
        if not tibia.player_is_fighting():
            if tibia.player.fought:
                tibia.player.loot()
            else:
                if tibia.starter_mark == tibia.max_markers:
                    tibia.starter_mark = 0
                else:
                    if not tibia.player_is_fighting():
                        if not tibia.is_in_mark_center():
                            tibia.starter_mark = tibia.starter_mark + 1

                    tibia.player.last_pos = tibia.player.position


def process(tibia):
    pass


def debug(tibia):
    print(tibia)
