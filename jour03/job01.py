class Ville:
    def __init__(self, name ="", nbpop = 0):
        self.__name = name
        self.__nbpop = nbpop

    def getnbpop(self):
        return self.__nbpop

    def setnbpop(self, value):
        self.__nbpop = value

    def getname(self):
        return self.__name

    def setname(self, value):
        self.__name = value


class Personne:
    def __init__(self, name, age, ville):
        self.name = name
        self.age = age
        self.ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.ville.setnbpop(self.ville.getnbpop() + 1)

Paris = Ville("Paris", 10000000)
Marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris: {Paris.getnbpop()} habitants\n"
      f"Population de la ville de Marseille: {Marseille.getnbpop()} habitants")

John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloé = Personne("Chloe", 18, Marseille)

print(f"Mise à jour de la population de la ville de Paris: {Paris.getnbpop()} habitants\n"
      f"Mise à jour de la population de la ville de Marseille: {Marseille.getnbpop()} habitants")
