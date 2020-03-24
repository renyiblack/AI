import threading
import action
import heal


class ThreadManager(threading.Thread):
    def __init__(self):
        super().__init__()
        self.action = action.Action()  # threading.Thread(target=self.a)
        self.action.daemon = True

        self.heal = heal.Heal()  # threading.Thread(target=self.h)
        self.heal.daemon = True

    def run(self):
        self.action.start()
        self.heal.start()
