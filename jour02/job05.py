class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche = False, reservoir = 50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, value):
        self.__kilometrage = value

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, value):
        self.__en_marche = value

    def get_modele(self):
        return self.__modele

    def set_modele(self, value):
        self.__modele = value

    def get_annee(self):
        return self.__annee

    def set_annee(self, value):
        self.__annee = value

    def get_marque(self):
        return self.__marque

    def set_marque(self, value):
        self.__marque = value

    def demarrer(self):
        self.__en_marche = True if self.__verifier_plein() > 5 else False

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir