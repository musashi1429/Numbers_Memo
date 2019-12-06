from player import Player
from sequence import Sequence


class Gamecontrol():
    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()

    def nameplayer(self):
        name = input("Merci d'entrer votre nom. --> ")
