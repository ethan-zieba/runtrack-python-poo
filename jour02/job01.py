class Rectangle:
    def __init__(self, length, width):
        self.__longueur = length
        self.__largeur = width

    def get_length(self):
        return self.__longueur

    def get_width(self):
        return self.__largeur

    def set_length(self, x):
        self.__longueur = x

    def set_width(self, x):
        self.__largeur = x

newrect = Rectangle(10, 5)
print(newrect.get_length(), newrect.get_width())
newrect.set_width(20)
print(newrect.get_length(), newrect.get_width())
