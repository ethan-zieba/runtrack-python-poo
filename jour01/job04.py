class Personne():
    def __init__(self, nom = "Toulmonde", prenom = "Monsieur"):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return (f"Je suis {self.prenom} {self.nom}")

john = Personne("Doe", "John")
jean = Personne("Dupond", "Jean")

print(jean.SePresenter())
print(john.SePresenter())