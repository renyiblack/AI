import keyboard
import os
import psutil
import sys
import thread_manager


class Ai():
    def __init__(self):
        # Set thread, daemon and start
        self.thread_manager = thread_manager.ThreadManager()

    def hunt(self):
        # Quit program on q press
        while(not keyboard.is_pressed('q')):
            # Save how much memory the program is using on a file
            memory_debug = open("../txt/memory_debug.txt", "a+")
            program = psutil.Process(os.getpid())
            memory_debug.write(f"{program.memory_info().rss}\n")

        print(">>> Stopped")


# Start bot
ai = Ai()
ai.hunt()
