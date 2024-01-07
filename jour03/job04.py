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

    def getposition(self):
        return self.position

    def getgoals(self):
        return self.goals
    def getpasses(self):
        return self.passes

    def getycards(self):
        return self.yellowcards

    def getrcards(self):
        return self.redcards

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
        self.listejoueurs[id].setid()
        self.listejoueurs[id].setid()
        self.listejoueurs[id].setid()
        self.listejoueurs[id].setid()
        self.listejoueurs[id].setid()
        self.listejoueurs[id].setid()
        self.listejoueurs[id].setid()