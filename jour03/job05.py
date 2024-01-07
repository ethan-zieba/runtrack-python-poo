from random import randint as rdint
from time import sleep as tsleep

class Personnage:
    def __init__(self, name, hp = 5, power = 1):
        self.name = name
        self.hp = hp
        self.power = power

    def getname(self):
        return self.name

    def setname(self, value):
        self.name = value

    def gethp(self):
        return self.hp

    def sethp(self, value):
        self.hp = value

    def getpower(self):
        return self.power

    def setpower(self, value):
        self.power = value

    def attack(self, enemy):
        attack, defence = self.getpower() + rdint(-2, 2), enemy.gethp()
        count = defence - attack if defence - attack > 0 else 0
        enemy.sethp(count)

class Arme:
    def __init__(self, name, power = 1):
        self.name = name
        self.power = power

    def getname(self):
        return self.name

    def setname(self, value):
        self.name = value

    def getpower(self):
        return self.power

    def setpower(self, value):
        self.power = value
class Jeu:
    def __init__(self):
        self.niveau = 1
        self.turnlist = []
        self.turnid = 0
        self.personnages = {}

    def startgame(self):
        self.niveau = int(input("Select a difficulty level (1 - 3): "))
        joueur = Personnage(input("Enter a name for your character: "), 20 // self.niveau, 9 // self.niveau)
        self.turnlist.append(joueur.getname())
        self.personnages[joueur.getname()] = joueur
        ennemi = Personnage("Pain au palpat", 10 * self.niveau, 5 * self.niveau)
        self.turnlist.append(ennemi.getname())
        self.personnages[ennemi.getname()] = ennemi
        self.turn()

    def isover(self):
        for p in self.personnages:
            if self.personnages[p].gethp() <= 0:
                return p
        else:
            return False

    def turn(self):
        while not self.isover():
            attacker, defender = self.personnages[self.turnlist[self.turnid]], self.personnages[self.turnlist[0 if self.turnid == 1 else 1]]
            print(f"{attacker.getname()} attacks {defender.getname()}")
            attacker.attack(defender)
            print(f"{attacker.getname()} has {attacker.gethp()} HP ! {defender.getname()} has {defender.gethp()} HP !")
            tsleep(2)
            self.turnid = 0 if self.turnid == 1 else 1
        print(f"{self.turnlist[0 if self.turnid == 1 else 1]} wins !")

jeu = Jeu()
jeu.startgame()
