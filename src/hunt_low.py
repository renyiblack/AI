import gc
import os
import sys
import keyboard
import psutil

from src.imagesearch import *
from src.loot import *
from src.heal import heal_low_lvl

'''
    Heal used is exura ico, to make cool down check works change pixel color to the desired spell
'''


def hunt_low(starter_mark, max_markers):
    img = ["../imgs/Markers/imagem1.png", "../imgs/Markers/imagem2.png", "../imgs/Markers/imagem3.png",
           "../imgs/Markers/imagem4.png", "../imgs/Markers/imagem5.png", "../imgs/Markers/imagem6.png",
           "../imgs/Markers/imagem7.png", "../imgs/Markers/imagem8.png", "../imgs/Markers/imagem9.png",
           "../imgs/Markers/imagem10.png", "../imgs/Markers/imagem11.png", "../imgs/Markers/imagem12.png",
           "../imgs/Markers/imagem13.png", "../imgs/Markers/imagem14.png", "../imgs/Markers/imagem15.png",
           "../imgs/Markers/imagem16.png", "../imgs/Markers/imagem17.png", "../imgs/Markers/imagem18.png",
           "../imgs/Markers/imagem19.png", "../imgs/Markers/imagem20.png"]

    # TODO try to find a formula to auto calculate positions

    # begin map

    # X, Y offset between 1920x1080(21:9) to 1366x768(16:9), to use this code on 1366x768 change offsets to 0
    offset_x = 554
    offset_y = 312
    offset_y_battle = 28

    map_x = 1198 + offset_x
    map_y = 27
    map_x1 = 1305 + offset_x
    map_y1 = 137

    # end map

    saved_x = 0
    saved_y = 0
    pyautogui.PAUSE = 0.000005
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
                if not pyautogui.pixelMatchesColor(459, 587 + offset_y, (63, 108, 154)):
                    heal_low_lvl()
                # look at battle list and see if first target is red or pink, if so, you're attacking
                if (pyautogui.pixelMatchesColor(1194 + offset_x, 428 + offset_y_battle, (255, 0, 0)) or
                        pyautogui.pixelMatchesColor(1194 + offset_x, 428 + offset_y_battle, (255, 128, 128))):
                    # If pixel at the top left corner of head on follow button is not green, click it
                    if not pyautogui.pixelMatchesColor(1350 + offset_x, 170, [104, 246, 104]):
                        pyautogui.click(1350 + offset_x, 170)  # follow
                        print(">>> Following...")
                    attacking = 1
                    pyautogui.moveTo(5, 5)  # moving mouse out of the way
                    # TODO spells()
                    print(">>> We're in battle!")
                else:
                    if attacking == 1:
                        print(">>> We've battled before this turn!")
                        attacking = 0
                        time.sleep(0.5)  # Delay in case the mob dies 1sqm from player
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
                            # See if battle list is empty(pixel at location where the top left corner of the monster
                            # hp bar should've be)
                            if not (pyautogui.pixelMatchesColor(1216 + offset_x, 443 + offset_y_battle, (64, 64, 64))):
                                print(">>> Battle list is not empty!")
                                if attacking == 0:
                                    print(">>> Attacking...")
                                    pyautogui.click(1216 + offset_x, 443 + offset_y_battle)  # attack
                                    # If pixel at the top corner of head on follow button is not green, click follow
                                    if not pyautogui.pixelMatchesColor(1350 + offset_x, 170, [104, 246, 104]):
                                        pyautogui.click(1350 + offset_x, 170)  # follow
                                        print(">>> Following...")
                                    attacking = 1
                                    # time.sleep(2) Timer to not change agree
                                # If pixel at top left corner in battle is white or black, something is hitting us
                                if ((pyautogui.pixelMatchesColor(1194 + offset_x, 428 + offset_y_battle, (0, 0, 0))
                                     or
                                     pyautogui.pixelMatchesColor(1194 + offset_x, 428 + offset_y_battle, (255, 255, 255)))):
                                    print(">>> Something is hitting us, hitting back...")
                                    pyautogui.click(1194, 428 + offset_y_battle)  # attack
                                    # If pixel at the top corner of head on follow button is not green, click follow
                                    if not pyautogui.pixelMatchesColor(1350 + offset_x, 170, [104, 246, 104]):
                                        pyautogui.click(1350 + offset_x, 170)  # follow
                                        print(">>> Following...")
                                    attacking = 1
                            else:
                                print(">>> Battle list is empty!")
                                # If we're not in mark center(1252, 82), move
                                if pos_x < (1251 + offset_x) or pos_x > (1253 + offset_x) or pos_y < 81 or pos_y > 83:
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
