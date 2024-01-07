class Tache:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = "En cours" if status == 0 else "Terminée"

    def gettitle(self):
        return self.title

    def settitle(self, value):
        self.title = value

    def getdescription(self):
        return self.description

    def setdescription(self, value):
        self.description = value

    def getstatus(self):
        return self.status

    def setstatus(self, value):
        self.status = "En cours" if value == 0 else "Terminée"


class ListeDeTaches:
    def __init__(self):
        self.liste = []

    def getliste(self):
        return self.liste

    def setliste(self, value):
        self.liste = value

    def ajouterTache(self, *taches):
        for task in taches:
            self.liste.append(task)

    def supprimerTache(self, taskname):
        for taskid in range(len(self.liste)):
            if self.liste[taskid].gettitle() == taskname:
                del self.liste[taskid]

    def marquerCommeFinie(self, taskname):
        for task in self.liste:
            if task.gettitle == taskname:
                task.setstatus(1)

    def afficherListe(self):
        print("\n")
        for taskid in range(len(self.liste)):
            print(f"ID: {taskid} Nom: {self.liste[taskid].gettitle()} Statut: {self.liste[taskid].getstatus()} Description: "
                  f"{self.liste[taskid].getdescription()}")

    def filtrerListe(self, filter):
        print(f"\nFilter: {filter}")
        for taskid in range(len(self.liste)):
            if self.liste[taskid].getstatus() == filter:
                print(f"ID: {taskid} Nom: {self.liste[taskid].gettitle()} Statut: {self.liste[taskid].getstatus()} Description: "
                    f"{self.liste[taskid].getdescription()}")

tache1 = Tache("Manger", "Manger poulet riz broccolis", 0)
tache2 = Tache("Boire", "De l'eau", 0)
tache3 = Tache("Courir", "8km au moins #militaire", 1)
tache4 = Tache("Dormir", "Courir en dormant #militaire", 1)


listetaches = ListeDeTaches()
listetaches.ajouterTache(tache1, tache2, tache3, tache4)
listetaches.afficherListe()
listetaches.filtrerListe("Terminée")