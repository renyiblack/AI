import action
import keyboard
import pyautogui
import os
import psutil
import sys
import threading


class Ai():
    def __init__(self):
        # Set thread, daemon and start
        self.action = action.Action() # threading.Thread(target=self.a)
        self.action.daemon = True
        self.action.start()

    def hunt(self):
        # Quit program on q press
        while(not keyboard.is_pressed('q')):
            # Save how much memory the program is using on a file
            memory_debug = open("..\\txt\\memory_debug.txt", "a+")
            program = psutil.Process(os.getpid())
            memory_debug.write(f"{program.memory_info().rss}\n")

        print(">>> Stopped")


# Start bot
ai = Ai()
ai.hunt()