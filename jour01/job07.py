class Personnage():
    def __init__(self, position = (0, 0)):
        self.position_coord  = [position[0], position[1]]

    def gauche(self):
        self.position_coord[0] -= 1

    def droite(self):
        self.position_coord[0] += 1

    def haut(self):
        self.position_coord[1] += 1

    def bas(self):
        self.position_coord[1] -= 1

    def position(self):
        return self.position_coord

obiwan_kenobrie = Personnage([0, 10])
print(obiwan_kenobrie.position())
obiwan_kenobrie.gauche()
print(obiwan_kenobrie.position())