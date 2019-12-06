from player import Player
from sequence import Sequence


class Gamecontrol():
    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()

    def nameplayer(self):
        name = input("Merci d'entrer votre nom. --> ")
        self.player.name = name
        print("Bonjour,{}".format(self.player.name))

    def levelplayer(self):
        level = int(input("Merci de choisir votre level entre 1 et 3 --> "))
        self.player.level = level
        print("Le niveau choisi est  : --> {}".format(self.player.level))
