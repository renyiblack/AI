import threading
import config
import imagesearch
import pyautogui
import time
import pywinauto
import player


class Action(threading.Thread):
    def run(self):
        fought = False
        coord = (-1,-1)
        count_trapado = 0
        
        while(True):
            # Are we fighting?
            if player.is_fighting():
                fought = True
                # Check if we are following
                player.follow()
            elif player.do_we_fight(fought):
                player.click('left', config.monster)
                player.follow()
            else:
                # Did we fight?
                if fought:
                    # Yes, loot
                    player.loot()
                    # We didn't fight this turn, we RICH BABY
                    fought = False
                else:
                    # No, did we reach end of the path?
                    if config.starter_mark == config.max_markers:
                        # Yes, reset
                        config.starter_mark = 0
                    else:
                        # No, move
                        coord, count_trapado = player.move(coord, count_trapado)
