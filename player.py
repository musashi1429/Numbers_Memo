import time
import os
class Player():

    def __init__(self):
        self.name = None
        self.level = None

    def udpatelevel(self,level):
        if level == 1:
            time.sleep(5)
        if level == 2:
             time.sleep(3)
        if level == 3:
            time.sleep(1)
