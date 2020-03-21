import pyautogui
import config

class heal:
    @staticmethod
    def heal():
        if not (pyautogui.pixelMatchesColor(config.life_bar_low[0],
                                            config.life_bar_low[1],
                                            config.life_low)):
            pyautogui.press('f1')
        else:
            if not (pyautogui.pixelMatchesColor(config.life_bar_high[0],
                                                config.life_bar_high[1],
                                                config.life_high)):
                pyautogui.press('f3')
            if not (pyautogui.pixelMatchesColor(
                    config.mana_bar[0], config.mana_bar[1], config.mana)):
                pyautogui.press('f2')