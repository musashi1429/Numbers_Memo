from random import *

class Sequence():
    def __init__(self):
        self.numbers = []

    def add_random_number(self):
        i = randint(1,100)
        self.numbers.append(i)
