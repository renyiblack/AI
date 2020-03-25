import threading
import action
import heal


class ThreadManager():
    def __init__(self):
        self.action = action.Action()  
        self.action.daemon = True
        self.action.start()

        self.heal = heal.Heal()
        self.heal.daemon = True
        self.heal.start()