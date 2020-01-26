import os

import keyboard
import psutil
import pyautogui

from coord import Coord
from imagesearch import imagesearcharea
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
                    # Search for mark on map, returns pos[0,0], needs to sum with original map[0,0]
                    tibia.mark.pair = imagesearcharea(tibia.markers[tibia.starter_mark],
                                                      tibia.map_begin.x,
                                                      tibia.map_begin.y,
                                                      tibia.map_end.x,
                                                      tibia.map_end.y)

                    tibia.player.position = Coord(
                        (tibia.map_begin.x + tibia.mark.x + 3, tibia.map_begin.y + tibia.mark.y + 3))

                    if not tibia.player_is_fighting():
                        if not tibia.are_we_in_map_center():
                            tibia.starter_mark = tibia.starter_mark + 1

                    tibia.player.last_pos = tibia.player.position


def process(tibia):
    pass


def debug(tibia):
    print(tibia)
