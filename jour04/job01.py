class Personne:
    def __init__(self, age = 14):
        self.age = age

    def getage(self):
        return self.age

    def setage(self, value):
        self.age = value

    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def getage(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age = 14, matiere = "Informatique"):
        super().__init__(age)
        self.matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")

eleve1 = Eleve()
print(eleve1.getage())
personne1 = Personne()

