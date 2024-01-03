class Livre:
    def __init__(self, title, author, pgnumber):
        self.__titre = title
        self.__auteur = author
        self.__nombrepages = pgnumber

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

livre1 = Livre("Voyage au bout de la nuit", "Ferdinand Céline", 700)
print(livre1.get_nombrepages())
livre1.set_nombrepages("Bonjour")