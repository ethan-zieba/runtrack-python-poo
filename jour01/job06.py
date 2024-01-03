class Animal():
    def __init__(self, age = 0, nom = ""):
        self.age = age
        self.nom = nom

    def viellir(self):
        self.age += 1

    def get_age(self):
        return (f"L'animal a {self.age} ans")

    def nommer(self, new_name):
        self.nom = new_name

    def get_name(self):
        return (f"L'animal s'appelle {self.nom}")


caramel = Animal()
print(caramel.get_age())
caramel.viellir()
print(caramel.get_age())
caramel.nommer("Caramel")
print(caramel.get_name())