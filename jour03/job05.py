class Personnage:
    def __init__(self, name, hp = 5, power = 1):
        self.name = name
        self.hp = hp
        self.power = power


class Arme:
    def __init__(self, name, power = 1):
        self.name = name
        self.power = power

class Jeu:
    def __init__(self):
        self.niveau = 1