import gc
import os
import sys
import keyboard
import psutil

from src.imagesearch import *
from src.loot import *
from src.heal import heal_low_lvl


def hunt_low(starter_mark, max_markers):
    img = ["../imgs/Markers/imagem1.png", "../imgs/Markers/imagem2.png", "../imgs/Markers/imagem3.png",
           "../imgs/Markers/imagem4.png", "../imgs/Markers/imagem5.png", "../imgs/Markers/imagem6.png",
           "../imgs/Markers/imagem7.png", "../imgs/Markers/imagem8.png", "../imgs/Markers/imagem9.png",
           "../imgs/Markers/imagem10.png", "../imgs/Markers/imagem11.png", "../imgs/Markers/imagem12.png",
           "../imgs/Markers/imagem13.png", "../imgs/Markers/imagem14.png", "../imgs/Markers/imagem15.png",
           "../imgs/Markers/imagem16.png", "../imgs/Markers/imagem17.png", "../imgs/Markers/imagem18.png",
           "../imgs/Markers/imagem19.png", "../imgs/Markers/imagem20.png"]

    '''
        To use on 1366x768(16:9) set offset to 0
        To use on 1920x1080(21:9) set offset_battle_x to 554 and offset_skills_y to 312
        
        Remember to change params on loot.py and heal.py too
    '''

    # begin params

    offset_battle_x = 0                         # 554
    offset_skills_y = 0                         # 312

    map_x = 1198 + offset_battle_x              # 1752(1920x1080)
    map_y = 27
    map_x1 = 1305 + offset_battle_x             # 1859(1920x1080)
    map_y1 = 137

    battle_x = 1194 + offset_battle_x           # 1748(1920x1080)
    battle_y = 456

    battle_mob_x = 1216 + offset_battle_x       # 1770(1920x1080)
    battle_mob_y = 471

    follow_x0 = 1350 + offset_battle_x          # 1904(1920x1080)
    follow_y0 = 170

    heal_x0 = 459
    heal_y0 = 587 + offset_skills_y             # 899(1920x1080)

    offset_pos_x1 = 1251 + offset_battle_x      # 1805(1920x1080)
    offset_pos_x2 = 1253 + offset_battle_x      # 1807(1920x1080)

    # end params

    saved_x = 0
    saved_y = 0
    pyautogui.PAUSE = 0.005
    pyautogui.FAILSAFE = False
    pyautogui.click(5, 5)
    attacking = 0
    on = 0

    memory_debug = open("../txt/memory_debug.txt", "a+")

    while on == 0:
        process = psutil.Process(os.getpid())
        try:
            if keyboard.is_pressed('q'):
                on = 1
                print(">>> q pressed!")
            else:
                # Blue color of exura ico in middle, right before the timer resets
                if not pyautogui.pixelMatchesColor(heal_x0, heal_y0, (63, 108, 154)):
                    heal_low_lvl()

                # look at battle list and see if first target is red or pink, if so, you're attacking
                if (pyautogui.pixelMatchesColor(battle_x, battle_y, (255, 0, 0)) or
                        pyautogui.pixelMatchesColor(battle_x, battle_y, (255, 128, 128))):

                    # If pixel at the top left corner of head on follow button is not green, click it
                    if not pyautogui.pixelMatchesColor(follow_x0, follow_y0, [104, 246, 104]):
                        pyautogui.click(follow_x0, follow_y0)  # follow
                        print(">>> Following...")

                    attacking = 1
                    pyautogui.moveTo(5, 5)  # moving mouse out of the way
                    # TODO spells()
                    print(">>> We're in battle!")
                else:
                    if attacking == 1:
                        print(">>> We've battled before this turn!")
                        attacking = 0
                        time.sleep(0.7)  # Delay in case the mob dies 1sqm from player
                        loot()
                        print(">>> all looted!")
                    else:
                        if starter_mark == max_markers:
                            starter_mark = 0
                            print(">>> Resetting!")
                        else:
                            print(">>> Looking for marker on map...")

                            # Search for mark on map, returns pos[0,0], needs to sum with original map[0,0]
                            coord_1, coord_2 = imagesearcharea(img[starter_mark], map_x, map_y, map_x1, map_y1)
                            pos_x = map_x + coord_1 + 3
                            pos_y = map_y + coord_2 + 3
                            '''
                                See if battle list is empty
                                Pixel at location where the top left corner of the monster hp bar should be
                            '''
                            if not (pyautogui.pixelMatchesColor(battle_mob_x, battle_mob_y, (64, 64, 64))):
                                print(">>> Battle list is not empty!")
                                if attacking == 0:
                                    print(">>> Attacking...")
                                    pyautogui.click(battle_mob_x, battle_mob_y)  # attack
                                    attacking = 1

                                    # If pixel at the top corner of head on follow button is not green, click follow
                                    if not pyautogui.pixelMatchesColor(follow_x0, follow_y0, [104, 246, 104]):
                                        pyautogui.click(follow_x0, follow_y0)  # follow
                                        print(">>> Following...")

                                # If pixel at top left corner in battle is white or black, something is hitting us
                                if ((pyautogui.pixelMatchesColor(battle_x, battle_y, (0, 0, 0))
                                     or
                                     pyautogui.pixelMatchesColor(battle_x, battle_y, (255, 255, 255)))):

                                    print(">>> Something is hitting us, hitting back...")
                                    pyautogui.click(battle_mob_x, battle_mob_y)  # attack
                                    attacking = 1

                                    # If pixel at the top corner of head on follow button is not green, click follow
                                    if not pyautogui.pixelMatchesColor(follow_x0, follow_y0, [104, 246, 104]):
                                        pyautogui.click(follow_x0, follow_y0)  # follow
                                        print(">>> Following...")
                            else:
                                print(">>> Battle list is empty!")
                                # If we're not in mark center(1252 + offset_battle_x, 82), move
                                if pos_x < offset_pos_x1 or pos_x > offset_pos_x2 or pos_y < 81 or pos_y > 83:
                                    if pos_x == saved_x and pos_y == saved_y:
                                        print(">>> Moving...")
                                        pyautogui.click(pos_x, pos_y)
                                        pyautogui.moveTo(5, 5)
                                        print(">>> Moved mouse out of the way")
                                else:
                                    starter_mark = starter_mark + 1

                            print(">>> Saving pos A and B...")
                            saved_x = pos_x
                            saved_y = pos_y
                            print(">>> saved!")
                            memory_debug.write(str(process.memory_info().rss) + "\n")
                            gc.collect()
        except MemoryError:
            '''
            If exception is found, rewrite HuntParam.txt with local information, last mark visited, in this case starter
            mark and maximum number of marks, in this case, max_markers. Then restart program with that data
            '''

            print(">>> Memory exception found, closing...")
            file = open("../txt/HuntParam.txt", "w")
            file.write("hunt low lvl\n")
            file.close()

            file = open("../txt/HuntParam.txt", "a")
            file.write(str(starter_mark) + "\n")
            file.write(str(max_markers))
            file.close()
            os.startfile(sys.argv[0])  # restart bot
            print(">>> closed!")

            sys.exit()
