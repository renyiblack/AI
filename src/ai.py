import os
import keyboard
import psutil
import pyautogui
import config as Cfg
import character


class AI(threading.Thread):
    starter_mark = Cfg.starter_mark
    max_markers = Cfg.max_markers
    running = True
    character = character.Character()

    def hunt(self):
        memory_debug = open("..\\txt\\memory_debug.txt", "a+")

        while self.running:
            program = psutil.Process(os.getpid())

            self.run()
            self.debug()

            memory_debug.write(
                f"{program.memory_info().rss} - {Cfg.starter_mark}\n")

    def run(self):
        
        else:
            # TODO ASYNC
            if not self.character.is_fighting(Cfg.tibia, Cfg.tibia_dialogs):
                if self.character.fought:
                    self.character.loot(Cfg.tibia, Cfg.tibia_dialogs, Cfg.obs)
                else:
                    if self.starter_mark == self.max_markers:
                        self.starter_mark = 0
                    elif self.character.is_in_mark_center(self.starter_mark, Cfg.tibia, Cfg.tibia_dialogs):
                        self.starter_mark = self.starter_mark + 1

    def debug(self):
        print("--------------------------------\n")
        print(f"(current mark)\n{self.starter_mark}\n"
              + f"(map begin)\n{Cfg.map_begin}\n"
              + f"(map end)\n{Cfg.map_end}\n"
              + f"(heal)\n{Cfg.heal}\n"
              + f"(follow)\n{Cfg.follow}\n"
              + f"(battle list)\n{Cfg.battle_list}\n")
        print("--------------------------------")



