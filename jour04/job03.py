class Rectangle:
    def __init__(self):
        self.__longueur = 1
        self.__largeur = 1

    def perimetre(self):
        return self.__longueur * 2 + self.__largeur * 2

    def surface(self):
        return self.__longueur * self.__largeur

    def getlongueur(self):
        return self.__longueur

    def setlongueur(self, value):
        self.__longueur = value

    def getlargeur(self):
        return self.__largeur

    def setlargeur(self, value):
        self.__largeur = value

class Parallelepipede(Rectangle):
    def __init__(self):
        super().__init__()
        self.__hauteur = 1

    def gethauteur(self):
        return self.__hauteur

    def sethauteur(self, value):
        self.__hauteur = value

    def volume(self):
        return self.getlargeur() * self.getlongueur() * self.__hauteur

para = Parallelepipede()
para.sethauteur(6)
para.setlongueur(4)
para.setlargeur(4)
print(para.volume())