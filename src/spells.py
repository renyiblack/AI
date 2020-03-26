import threading
import pyautogui
import config
import time

# TODO remove sleeps and check CD


class Spells(threading.Thread):
    def run(self):
        while(True):
            self.heal()

    def heal(self):
        # Low Life?
        if not (pyautogui.pixelMatchesColor(config.life_bar_low[0], config.life_bar_low[1], config.life)):
            print(f"life: {config.life_bar_low}")
            print(">>> needs bigger heal")
            config.tibia[config.xming[1]].type_keys('{VK_F1}')
            time.sleep(1)
        else:
            # Needs minor heal?
            if not (pyautogui.pixelMatchesColor(config.life_bar_high[0], config.life_bar_high[1], config.life)):
                print(">>> needs minor heal")
                config.tibia[config.xming[1]].type_keys('{VK_F1}')
                time.sleep(1)
            # Needs mana?
            if not (pyautogui.pixelMatchesColor(config.mana_bar[0], config.mana_bar[1], config.mana)):
                print(f"mana: {config.mana_bar}")
                print(">>> needs mana")
                config.tibia[config.xming[1]].type_keys('{VK_F2}')
