from random import randint
from time import sleep

class Carte:
    def __init__(self, value, color):
        self.value = value
        colorlist = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.color = colorlist[color]

    def __repr__(self):
        figureslist = ["Jack", "Queen", "King"]
        return f'Card ({self.value if self.value < 11 else figureslist[self.value - 11]} of {self.color})'

    def getvalue(self):
        return self.value if self.value <= 10 else 10

    def setvalue(self, value):
        self.value = value

    def getcolor(self):
        return self.color

    def setcolor(self, value):
        self.color = value


class Deck:
    def __init__(self):
        self.decklist = []

    def filldeck(self):
        for i in range(1, 14):
            for u in range(4):
                self.decklist.append(Carte(i, u))

    def shuffledeck(self):
        for i in range(52):
            rdposition = randint(0, 51)
            self.decklist[i], self.decklist[rdposition] = self.decklist[rdposition], self.decklist[i]

    def getdecklist(self):
        return self.decklist

    def totalvalue(self):
        total = 0
        for e in self.decklist:
            total += e.getvalue() if e.getvalue() != 1 else (11 if e.getvalue() == 1 and total + 11 <= 21 else 1)
        return total

    def drawcard(self):
        topcard = self.decklist[0]
        self.decklist.pop(0)
        return topcard

    def addcard(self, card):
        self.decklist.append(card)

class Jeu:

    def __init__(self):
        self.deck = Deck()
        self.dealerdeck = Deck()
        self.playerdeck = Deck()
        self.startgame()

    def startgame(self):
        self.deck.filldeck()
        self.deck.shuffledeck()
        self.turn(0)

    def checkover(self):
        if self.playerdeck.totalvalue() == 21:
            return "Win"
        if self.playerdeck.totalvalue() > 21:
            return "Lose"
        if self.dealerdeck.totalvalue() == 21:
            return "Lose"
        if self.dealerdeck.totalvalue() > 21:
            return "Win"
        if 21 >= self.dealerdeck.totalvalue() >= 17 and self.playerdeck.totalvalue() > self.dealerdeck.totalvalue():
            return "Win"
        if 21 >= self.dealerdeck.totalvalue() >= 17 and self.playerdeck.totalvalue() < self.dealerdeck.totalvalue():
            return "Lose"


    def turn(self, who):
        stops = False
        while self.checkover() not in ["Win", "Lose"]:

            who = 1 if who == 0 else 0
            if who == 1 and not stops:
                draw = str(input("Do you want to draw ? y/n ")).lower()
                if draw == "n":
                    stops = True
                    pass
                else:
                    drawcard = self.deck.drawcard()
                    sleep(1)
                    print(f"Player draws a {drawcard}")
                    self.playerdeck.addcard(drawcard)
                    print(f"Player now has {self.playerdeck.getdecklist()}")
                    print(f"Total value of Player deck: {self.playerdeck.totalvalue()}")
            else:
                if self.dealerdeck.totalvalue() >= 17:
                    print("Dealer stops playing")
                else:
                    drawcard = self.deck.drawcard()
                    sleep(1)
                    print(f"Dealer draws a {drawcard}")
                    self.dealerdeck.addcard(drawcard)
                    print(f"Dealer now has {self.dealerdeck.getdecklist()}")
                    print(f"Total value of Dealer deck: {self.dealerdeck.totalvalue()}")

        print(self.checkover())

game = Jeu()