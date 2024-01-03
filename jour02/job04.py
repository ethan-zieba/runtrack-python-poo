class Student:
    def __init__(self, name, lastname, id, credits = 0):
        self.__name = name
        self.__lastname = lastname
        self.__credits = credits
        self.__id = id
        self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très Bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, value):
        self.__lastname = value

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_credits(self):
        return self.__credits

    def set_credits(self, value):
        self.__credits = value

    def add_credit(self, value):
        if value >= 0: self.__credits += value
        else:
            raise Exception("Value added must be greater than 0")

    def student_info(self):
        return(f"Nom = {self.__lastname}\nPrenom = {self.__name}\nID = {self.__id}\nNiveau = {self.__level}")

student1 = Student("John", "Doe", 145, 20)
print(student1.student_info())
student1.add_credit(20)
student1.add_credit(2)
student1.add_credit(2)
print(f"Le nombre de crédits de {student1.get_name()} {student1.get_lastname()} est de {student1.get_credits()} point{'s' if student1.get_credits() > 1 else ''}")
print(student1.student_info())
