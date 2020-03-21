import threading
import keyboard
import config as Cfg
import ai


class Bot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.ai = ai.Ai()

    def run(self):
        if not Cfg.hunt.lower() == "hunt":
            print(">>> Hunt not defined!")
            return

        while not keyboard.is_pressed('q'):
            return

def main():
    bot = Bot()
    bot.daemon = True
    bot.start
       


if __name__ == '__main__':
    main()
