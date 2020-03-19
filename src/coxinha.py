import threading
import time

import tibia


class Coxinha(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def heal(self):
        print("yo")

    def run(self):
        while (True):
            time.sleep(0.3)
            self.heal()
