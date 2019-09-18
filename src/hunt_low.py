import gc
import os
import sys
import keyboard
import psutil

from src.imagesearch import *
from src.loot import *
from src.heal import heal_low_lvl
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

    offset_battle_x = 0  # 554
    offset_skills_y = 0  # 312

    cap_x = 149  # TODO check coord in 1920x1080
    cap_y = 378  # TODO check coord in 1920x1080

    map_x = 1198 + offset_battle_x  # 1752(1920x1080)
    map_y = 27
    map_x1 = 1305 + offset_battle_x  # 1859(1920x1080)
    map_y1 = 137

    battle_x = 1194 + offset_battle_x  # 1748(1920x1080)
    battle_y = 456

    battle_mob_x = 1216 + offset_battle_x  # 1770(1920x1080)
    battle_mob_y = 471

    follow_x0 = 1350 + offset_battle_x  # 1904(1920x1080)
    follow_y0 = 170

    heal_x0 = 459
    heal_y0 = 587 + offset_skills_y  # 899(1920x1080)

    offset_pos_x1 = 1251 + offset_battle_x  # 1805(1920x1080)
    offset_pos_x2 = 1253 + offset_battle_x  # 1807(1920x1080)

    # end params

    # begin colors

    red = (255, 0, 0)  # Red battle list when we're in battle
    pink = (255, 128, 128)  # Pink battle list when we're in battle
    gray = (64, 64, 64)  # Gray battle list in the beginning of monster hp bar
    black = (255, 255, 255)  # Black battle list when monster hits us
    green_follow = (104, 246, 104)  # Green color, head left pixel
    exura_blue = (63, 108, 154)  # Blue color of exura ico in middle TODO change this color
    white_cap = (192, 192, 192)  # White color of 0 cap in skills tab

    # end colors

    # stopped = 0
    saved_x = 0
    saved_y = 0
    attacking = 0
    on = 0

    # pyautogui.PAUSE = 0.05 value used for debug
    pyautogui.PAUSE = 0.0000005
    pyautogui.FAILSAFE = False
    pyautogui.click(5, 5)

    # TODO create class coord

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
                #    sell_loot(10, img, map_x, map_y, map_x1, map_y1, offset_pos_x1, offset_pos_x2)

                # TODO change to shade of blue when not on cd and remove not
                # Can we heal?
                # if not pyautogui.pixelMatchesColor(heal_x0, heal_y0, exura_cd_blue):
                heal_low_lvl()

                # Are we fighting?
                if (pyautogui.pixelMatchesColor(battle_x, battle_y, red) or
                        pyautogui.pixelMatchesColor(battle_x, battle_y, pink)):

                    # Set attacking
                    attacking = 1

                    # Are we following?
                    if not pyautogui.pixelMatchesColor(follow_x0, follow_y0, green_follow):
                        pyautogui.click(follow_x0, follow_y0)
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
                            coord_1, coord_2 = imagesearcharea(img[starter_mark], map_x, map_y, map_x1, map_y1)
                            pos_x = map_x + coord_1 + 3
                            pos_y = map_y + coord_2 + 3

                            # There're monsters nearby!
                            if not (pyautogui.pixelMatchesColor(battle_mob_x, battle_mob_y, gray)):

                                # Hit it!
                                if attacking == 0:
                                    # Attack!
                                    pyautogui.click(battle_mob_x, battle_mob_y)
                                    attacking = 1

                                    # Are we following?
                                    if not pyautogui.pixelMatchesColor(follow_x0, follow_y0, green_follow):
                                        pyautogui.click(follow_x0, follow_y0)

                                    # Move mouse away!
                                    pyautogui.moveTo(5, 5)

                                # TODO change to elif
                                # Are we being hit?
                                if (pyautogui.pixelMatchesColor(battle_x, battle_y, black)) and attacking == 0:

                                    # Attack!
                                    pyautogui.click(battle_mob_x, battle_mob_y)
                                    attacking = 1

                                    # Are we following?
                                    if not pyautogui.pixelMatchesColor(follow_x0, follow_y0, green_follow):
                                        pyautogui.click(follow_x0, follow_y0)

                                    # Move mouse away!
                                    pyautogui.moveTo(5, 5)
                            # We're not in combat!
                            else:
                                # Are we in mark center(1252 + offset_battle_x, 82)?
                                if pos_x < offset_pos_x1 or pos_x > offset_pos_x2 or pos_y < 81 or pos_y > 83:
                                    if pos_x == saved_x and pos_y == saved_y:
                                        coord_1, coord_2 = imagesearcharea(img[starter_mark], map_x, map_y, map_x1,
                                                                           map_y1)
                                        pos_x = map_x + coord_1 + 3
                                        pos_y = map_y + coord_2 + 3
                                        pyautogui.click(pos_x, pos_y)
                                        pyautogui.moveTo(5, 5)

                                # We're! Next mark and save memory use
                                else:
                                    starter_mark = starter_mark + 1
                                    memory_debug.write(str(process.memory_info().rss) + "-" + str(starter_mark) + "\n")

                            saved_x = pos_x
                            saved_y = pos_y
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
