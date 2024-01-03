from math import pi


class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, new):
        self.rayon = new

    def aire(self):
        return pi * (self.rayon * self.rayon)

    def circonference(self):
        return pi * (2 * self.rayon)

    def diametre(self):
        return self.rayon * 2

    def afficherInfos(self):
        return (f"Aire: {self.aire()}, Circonference: {self.circonference()}, Diametre: {self.diametre()}")

cercle4 = Cercle(4)
cercle7 = Cercle(7)

print(cercle4.afficherInfos())
print(cercle7.afficherInfos())
