class CompteBancaire:
    def __init__(self, accid, name, firstname, balance, agios, decouvert = True):
        self.__id = accid
        self.__name = name
        self.__firstname = firstname
        self.__balance = balance
        self.__decouvert = decouvert
        self.__agios = agios

    def afficher(self):
        return (f"ID: {self.__id}\nNom et prénom: {self.__name} {self.__firstname}\nSolde: {self.__balance}")

    def afficherSolde(self):
        return (f"Solde: {self.__balance}")

    def versement(self, value):
        self.__balance += value

    def retrait(self, value):
        self.__balance -= value if self.__balance - value >= 0 or self.__decouvert == True else self.__balance
        self.agios()

    def agios(self):
        if self.__balance < 0:
            self.__balance -= self.__agios

    def virement(self, destinataire, value):
        if self.__balance - value >= 0 or self.__decouvert == True:
            self.retrait(value)
            destinataire.versement(value)
            print("Virement effectué")
        else:
            print("Solde indisponible")

compte1 = CompteBancaire(1, "Doe", "John", 1000, 80, True)
compte2 = CompteBancaire(2, "Dupont", "Jean", 120, 80, True)

print(compte1.afficher(), "\n", compte2.afficher())

compte1.virement(compte2, 200)

print(compte1.afficher(), "\n", compte2.afficher())

compte1.virement(compte2, 900)

print(compte1.afficher(), "\n", compte2.afficher())

