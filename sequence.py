from random import *
#add number for a cycle
class Sequence():
    def __init__(self):
        self.numbers = [1,]

    def add_random_number(self):
        i = randint(1,100)
        self.numbers.append(i)
