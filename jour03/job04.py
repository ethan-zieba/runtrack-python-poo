class Joueur:
    def __init__(self, name, id, position, goals, passes, yellowcards, redcards):
        self.name = name
        self.id = id
        self.position = position
        self.goals = goals
        self.passes = passes
        self.yellowcards = yellowcards
        self.redcards = redcards

    def getid(self):
        return self.id

    def setid(self, value):
        self.id = value

    def setname(self, value):
        self.name = value

    def getposition(self):
        return self.position

    def setposition(self, value):
        self.position = value

    def getgoals(self):
        return self.goals

    def setgoals(self, value):
        self.goals = value

    def getpasses(self):
        return self.passes

    def setpasses(self, value):
        self.passes = value

    def getycards(self):
        return self.yellowcards

    def setycards(self, value):
        self.yellowcards = value

    def getrcards(self):
        return self.redcards

    def setrcards(self, value):
        self.redcards = value

    def marquerUnBut(self):
        self.goals += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.yellowcards += 1

    def recevoirUnCartonRouge(self):
        self.redcards += 1

    def afficherStatistiques(self):
        print(f"Nom: {self.name} Numéro: {self.id} Position: {self.position} Passes dé: {self.passes} Buts: {self.goals}"
              f"Cartons jaunes: {self.yellowcards} Cartons rouges: {self.redcards}")

class Equipe:
    def __init__(self):
        self.listejoueurs = {}

    def ajouterJoueur(self, joueur):
        self.listejoueurs[joueur.getid()] = joueur

    def AfficherStatistiquesJoueur(self):
        for e in self.listejoueurs:
            print(f"{self.listejoueurs[e].getid()}{self.listejoueurs[e].getname()}{self.listejoueurs[e].getposition()}"
                  f"{self.listejoueurs[e].getgoals()}{self.listejoueurs[e].getpasses()}"
                  f"{self.listejoueurs[e].getycards()}{self.listejoueurs[e].getrcards()}")

    def mettreAJourStatistiquesJoueurs(self, id):
        self.listejoueurs[id].setid(input("Numéro: "))
        self.listejoueurs[id].setgoals(input("Buts: "))
        self.listejoueurs[id].setpasses(input("Passes: "))
        self.listejoueurs[id].setycards(input("Cartons jaunes: "))
        self.listejoueurs[id].setrcards(input("Cartons rouges: "))
        self.listejoueurs[id].setposition(input("Position: "))
        self.listejoueurs[id].setname(input("Nom: "))
