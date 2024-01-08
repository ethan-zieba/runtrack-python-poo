class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def getmarque(self):
        return self.marque

    def setmarque(self, value):
        self.marque = value

    def getmodele(self):
        return self.modele

    def setmodele(self, value):
        self.modele = value

    def getannee(self):
        return self.annee

    def setannee(self, value):
        self.annee = value

    def getprix(self):
        return self.prix

    def setprix(self, value):
        self.prix = value

    def informationsVehicule(self):
        print(f"Marque = {self.getmarque()}\nModele = {self.getmodele()}\n"
              f"Année = {self.getannee()}\nPrix = {self.getprix()}")

    def demarrer(self):
        print("Attention je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def getportes(self):
        return self.portes

    def setportes(self, value):
        self.portes = value

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.getportes()}")

    def demarrer(self):
        print("Attention je roule avec 2 tonnes 4 de ferraille")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print("Attention je roule avec 190kg de bonheur")

bmw = Voiture("BMW", "I34", 2020, 182912, 4)
bmw.informationsVehicule()
bmw.demarrer()
suzuki = Moto("Suzuki", "GSXR1000", 2019, 500, 2)
suzuki.informationsVehicule()
suzuki.demarrer()