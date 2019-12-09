from player import Player
from sequence import Sequence
import time
import os

#Class for control every fonction of game
class Gamecontrol():

    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()
#tahke name information
    def nameplayer(self):
        name = input("Merci d'entrer votre nom. --> ")
        self.player.name = name
        print("Bonjour,{}".format(self.player.name))
        time.sleep( 1 )
        os.system("clear")
#take level choice
    def levelplayer(self):
        level = int(input("Merci de choisir votre level entre 1 et 3 --> "))
        self.player.level = level
        print("Le niveau choisi est  : --> {}".format(self.player.level))
        time.sleep( 1 )
        os.system("clear")
#boucle for chek list
    def addnumber(self):
        self.sequence.add_random_number()

    def playeraddnumber(self):
        for i in self.sequence.numbers:
            self.listplayer.append(int(input()))
            os.system("clear")
        for z in self.listplayer:
            if z == z in
            self.listplayer(self):
                self.listplayer.replace(z)
                os.system("clear")
        print(self.sequence.numbers)
        print(self.listplayer)

    def listsequence(self):
        for i in self.sequence.numbers:
            print(i)
            self.player.udpatelevel(self.player.level)
            os.system("clear")
        print( "End : %s" % time.ctime())

    def replace(self):
        for i in self.listplayer:
            if i in self.listplayer.append(int(input())) == z in self.listplayer:
                if i == z:
                    i.replace(listplayer)


#list of input player
    def listplayer(self):
        self.listplayer = []
        listplayer =set(self.listplayer)
        for i in self.sequence.numbers:
            self.listplayer.append(int(input()))
            os.system("clear")
        print(self.sequence.numbers)
        print(self.listplayer)
#for add number
    def appendnumbers(self):
        while len(self.sequence.numbers) == len(self.listplayer):
            self.sequence.add_random_number()
            self.listsequence()
            self.playeraddnumber()
        if len(self.sequence.numbers) == len(self.listplayer):
            self.playeraddnumber()
            print("K.o")
            print(self.sequence.numbers)

    def boucle(self):
        while len(self.sequence.numbers)  == len(self.listplayer):
            os.system("clear")
            self.listsequence()
            self.playeraddnumber()
            self.sequence.add_random_number()
