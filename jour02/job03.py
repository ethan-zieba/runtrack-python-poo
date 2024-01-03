class Livre:
    def __init__(self, title, author, pgnumber, available = True):
        self.__titre = title
        self.__auteur = author
        self.__nombrepages = pgnumber
        self.__disponible = available

    def get_titre(self):
        return self.__titre

    def set_titre(self, value):
        self.__titre = value

    def get_nombrepages(self):
        return self.__nombrepages

    def set_nombrepages(self, value):
        try:
            value = int(value)
        except (ValueError):
            print("ERROR: Page Number must be an integer")
        self.__nombrepages = value

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, value):
        self.__auteur = value

    def get_disponible(self):
        return self.__disponible

    def emprunter(self):
        self.__disponible = False if self.__disponible == True else False

    def rendre(self):
        self.__disponible = True if self.__disponible == False else True



livre1 = Livre("Voyage au bout de la nuit", "Ferdinand Céline", 700)
print(livre1.get_disponible())
livre1.emprunter()
print(livre1.get_disponible())
livre1.rendre()
print(livre1.get_disponible())
