from random import randint

class Carte:
    def __init__(self, value, color):
        self.value = value
        colorlist = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.color = colorlist[color]

    def __repr__(self):
        figureslist = ["Jack", "Queen", "King"]
        return f'Card ({self.value if self.value < 11 else figureslist[self.value - 11]} of {self.color})'

    def getvalue(self):
        return self.value

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
        print(self.decklist)

    def shuffledeck(self):
        for i in range(52):
            rdposition = randint(0, 52)
            self.decklist[i], self.decklist[rdposition] = self.decklist[rdposition], self.decklist[i]

    def getdecklist(self):
        return self.decklist

deck = Deck()
deck.filldeck()
deck.shuffledeck()
print(deck.getdecklist())