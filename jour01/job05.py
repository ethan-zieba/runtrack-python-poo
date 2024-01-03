class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        return self.x, self.y
    def afficherX(self):
        return(self.x)
    def afficherY(self):
        return(self.y)
    def changerX(self, new):
        self.x = new
    def changerY(self, new):
        self.y = new

