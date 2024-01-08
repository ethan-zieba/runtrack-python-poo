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

class Cercle(Forme):
    def __init__(self):
        self.radius = 2

    def getradius(self):
        return self.radius

    def setradius(self, value):
        self.radius = value

    def aire(self):
        return self.radius * self.radius * 3.1415

rect = Rectangle()
rect.setlargeur(10)
rect.setlongueur(4)
print(rect.aire())
circ = Cercle()
circ.setradius(10)
print(circ.aire())