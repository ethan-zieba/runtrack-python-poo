class Commande:
    def __init__(self, id, dishes = {}, status = "En cours"):
        self.__id = id
        self.__dishes = dishes
        self.__status = status

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_dishes(self):
        return self.__dishes

    def set_dishes(self, value):
        self.__dishes = value

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    def add_dish(self, name, price):
        self.get_dishes().update({name:price})

    def annuler(self):
        self.set_status("Annulée")

    def __total_commande(self):
        total = 0
        for e in self.get_dishes():
            total += self.get_dishes()[e]
        return total

    def with_tva(self):
        return self.__total_commande() + self.__total_commande() * 0.21

    def afficher_commande(self):
        return(f"ID: {self.get_id()}\nPlats: {self.get_dishes()}\nPrix total HT: {self.__total_commande()}\nPrix total: "
               f"{self.with_tva()}\nStatut: {self.get_status()}")

commande1 = Commande(1)
commande1.add_dish("Soupe", 200)
print(commande1.get_dishes())
print(commande1.afficher_commande())
commande1.add_dish("Viande", 500)
print(commande1.afficher_commande())
commande1.annuler()
print(commande1.afficher_commande())
