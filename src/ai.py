import threading
import player
import spells
import keyboard
import os
import psutil
import sys

player_thread = player.Player()
player_thread.daemon = True
player_thread.start()

spells_thread = spells.Spells()
spells_thread.daemon = True
spells_thread.start()

print(">>> running")

# Quit program on q press
while(not keyboard.is_pressed('q')):
    # Save how much memory the program is using on a file
    memory_debug = open("../txt/memory_debug.txt", "a+")
    program = psutil.Process(os.getpid())
    memory_debug.write(f"{program.memory_info().rss}\n")

print(">>> stopped")
