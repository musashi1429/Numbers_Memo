from player import Player
from sequence import Sequence
import time
import os


class Gamecontrol():
    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()

    def nameplayer(self):
        name = input("Merci d'entrer votre nom. --> ")
        self.player.name = name
        print("Bonjour,{}".format(self.player.name))
        time.sleep( 1 )
        os.system("clear")

    def levelplayer(self):
        level = int(input("Merci de choisir votre level entre 1 et 3 --> "))
        self.player.level = level
        print("Le niveau choisi est  : --> {}".format(self.player.level))
        time.sleep( 1 )
        os.system("clear")

    def listsequence(self):
        self.sequence.add_random_number()
        for i in self.sequence.numbers:
            print(i)
            time.sleep( 5 )
            os.system("clear")
        print( "End : %s" % time.ctime())
