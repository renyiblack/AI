import gc
import os
import sys
import keyboard
import psutil

from src.imagesearch import *
from src.loot import *
from src.heal import heal_low_lvl
from src.coord import Coord


# from src.sell_loot import sell_loot


def hunt_low(starter_mark, max_markers):
    img = ['../imgs/Markers/imagem1.png', '../imgs/Markers/imagem2.png', '../imgs/Markers/imagem3.png',
           '../imgs/Markers/imagem4.png', '../imgs/Markers/imagem5.png', '../imgs/Markers/imagem6.png',
           '../imgs/Markers/imagem7.png', '../imgs/Markers/imagem8.png', '../imgs/Markers/imagem9.png',
           '../imgs/Markers/imagem10.png', '../imgs/Markers/imagem11.png', '../imgs/Markers/imagem12.png',
           '../imgs/Markers/imagem13.png', '../imgs/Markers/imagem14.png', '../imgs/Markers/imagem15.png',
           '../imgs/Markers/imagem16.png', '../imgs/Markers/imagem17.png', '../imgs/Markers/imagem18.png',
           '../imgs/Markers/imagem19.png', '../imgs/Markers/imagem20.png']

    '''
        To use on 1366x768(16:9) set offsets to 0
        To use on 1920x1080(21:9) set offset_battle_x to 554 and offset_skills_y to 312
        
        Remember to change params on loot.py and heal.py too
    '''

    # begin params

    offset_battle = Coord(0, 0)
    offset_skills = Coord(0, 0)

    # offset_battle_x = 0  # 554
    # offset_skills_y = 0  # 312

    cap_x = 149  # TODO check coord in 1920x1080
    cap_y = 378  # TODO check coord in 1920x1080

    map_begin = Coord(1198 + offset_battle.x, 27)
    map_end = Coord(1350 + offset_battle.x, 137)

    # map_x = 1198 + offset_battle_x  # 1752(1920x1080)
    # map_y = 27
    # map_x1 = 1305 + offset_battle_x  # 1859(1920x1080)
    # map_y1 = 137

    battle_list = Coord(1194 + offset_battle.x, 456)

    # battle_x = 1194 + offset_battle_x  # 1748(1920x1080)
    # battle_y = 456

    mob_battle = Coord(1216 + offset_battle.x, 471)

    # battle_mob_x = 1216 + offset_battle_x  # 1770(1920x1080)
    # battle_mob_y = 471

    follow = Coord(1350 + offset_battle.x, 170)

    # follow_x0 = 1350 + offset_battle_x  # 1904(1920x1080)
    # follow_y0 = 170

    heal = Coord(459, 587 + offset_skills.y)

    # heal_x0 = 459
    # heal_y0 = 587 + offset_skills_y  # 899(1920x1080)

    click_left = 1251 + offset_battle.x  # 1805(1920x1080)
    click_right = 1253 + offset_battle.x  # 1807(1920x1080)
    click_down = 83
    click_up = 81

    # end params

    # begin colors

    red = (255, 0, 0)  # Red battle list when we're in battle
    pink = (255, 128, 128)  # Pink battle list when we're in battle
    gray = (64, 64, 64)  # Gray battle list in the beginning of monster hp bar
    black = (255, 255, 255)  # Black battle list when monster hits us
    green_follow = (104, 246, 104)  # Green color, head left pixel
    exura_blue = (63, 108, 154)  # Blue color of exura ico in middle
    white_cap = (192, 192, 192)  # White color of 0 cap in skills tab

    # end colors

    # stopped = 0
    marker = Coord(0, 0)
    pos = Coord(0, 0)
    saved_pos = Coord(0, 0)
    attacking = 0
    on = 0

    # pyautogui.PAUSE = 0.05 value used for debug
    pyautogui.PAUSE = 0.000005
    pyautogui.FAILSAFE = False
    pyautogui.click(5, 5)

    memory_debug = open("../txt/memory_debug.txt", "a+")

    # Starting hunt
    while on == 0:
        # Tracking memory use
        process = psutil.Process(os.getpid())
        try:
            # Quit hunt
            if keyboard.is_pressed('q'):
                on = 1
            # Hunting
            else:
                # TODO make it check cap and sell loot
                # Do we have cap?
                # if pyautogui.pixelMatchesColor(cap_x, cap_y, white_cap):
                #    sell_loot(10, img, map_x, map_y, map_x1, map_y1, click_left, click_right)

                # Can we heal?
                if pyautogui.pixelMatchesColor(heal.x, heal.y, exura_blue):
                    heal_low_lvl()

                # Are we fighting?
                if (pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, red) or
                        pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, pink)):

                    # Set attacking
                    attacking = 1

                    # Are we following?
                    if not pyautogui.pixelMatchesColor(follow.x, follow.y, green_follow):
                        pyautogui.click(follow.x, follow.y)
                        pyautogui.moveTo(5, 5)

                    # TODO spells()

                    '''
                        # Are we moving?
                        if pos_x == saved_x and pos_y == saved_y:
                            stopped = stopped + 1
                            if stopped == 10:
                                pyautogui.click(pos_x, pos_y)
                        else:
                            stopped = 0
                    '''

                # Are we out of combat?
                else:
                    # Did we fight before?
                    if attacking == 1:
                        # Reset attacking and wait 0.7s to get close to mob before looting
                        attacking = 0
                        time.sleep(0.7)
                        loot()
                    else:
                        # Did we reach end of path?
                        if starter_mark == max_markers:
                            starter_mark = 0
                        else:
                            # Search for mark on map, returns pos[0,0], needs to sum with original map[0,0]
                            marker.x, marker.y = imagesearcharea(img[starter_mark],
                                                                 map_begin.x, map_begin.y, map_end.x, map_end.y)
                            pos.x = map_begin.x + marker.x + 3
                            pos.y = map_begin.y + marker.y + 3

                            # There're monsters nearby!
                            if not (pyautogui.pixelMatchesColor(mob_battle.x, mob_battle.y, gray)):

                                # Hit it!
                                if attacking == 0:
                                    # Attack!
                                    pyautogui.click(mob_battle.x, mob_battle.y)
                                    attacking = 1

                                    # Are we following?
                                    if not pyautogui.pixelMatchesColor(follow.x, follow.y, green_follow):
                                        pyautogui.click(follow.x, follow.y)

                                    # Move mouse away!
                                    pyautogui.moveTo(5, 5)

                                # TODO comment this, have no effect. Maybe create func imhit?
                                # Are we being hit?
                                elif pyautogui.pixelMatchesColor(battle_list.x, battle_list.y, black):

                                    # Attack!
                                    pyautogui.click(battle_list.x, battle_list.y)
                                    attacking = 1

                                    # Are we following?
                                    if not pyautogui.pixelMatchesColor(follow.x, follow.y, green_follow):
                                        pyautogui.click(follow.x, follow.y)

                                    # Move mouse away!
                                    pyautogui.moveTo(5, 5)
                            # We're not in combat!
                            else:
                                # Are we in mark center(1252 + offset_battle_x, 82)?
                                if pos.x < click_left or pos.x > click_right or pos.y < click_up or pos.y > click_down:
                                    if pos == saved_pos:
                                        marker.x, marker.y = imagesearcharea(img[starter_mark],
                                                                             map_begin.x, map_begin.y,
                                                                             map_end.x, map_end.y)
                                        pos.x = map_begin.x + marker.x + 3
                                        pos.y = map_begin.y + marker.y + 3
                                        pyautogui.click(pos.x, pos.y)
                                        pyautogui.moveTo(5, 5)

                                # We're! Next mark and save memory use
                                else:
                                    starter_mark = starter_mark + 1
                                    memory_debug.write(str(process.memory_info().rss) + "-" + str(starter_mark) + "\n")

                            saved_pos = pos
                            gc.collect()
        except MemoryError:
            '''
            If exception is found, rewrite HuntParam.txt with hunt information, last mark visited and maximum number of 
            marks. Then restart the program with that data
            
            Obs.: This only works in windows
            '''

            file = open("../txt/HuntParam.txt", "w")
            file.write("hunt low lvl\n")
            file.close()

            file = open("../txt/HuntParam.txt", "a")
            file.write(str(starter_mark) + "\n")
            file.write(str(max_markers))
            file.close()
            os.startfile(sys.argv[0])

            sys.exit()
