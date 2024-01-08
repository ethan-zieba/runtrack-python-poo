class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self):
        self.largeur = 0
        self.longueur = 0

    def getlongueur(self):
        return self.longueur

    def setlongueur(self, value):
        self.longueur = value

    def getlargeur(self):
        return self.largeur

    def setlargeur(self, value):
        self.largeur = value

    def aire(self):
        return self.longueur * self.largeur

rect = Rectangle()
rect.setlargeur(10)
rect.setlongueur(4)
print(rect.aire())
