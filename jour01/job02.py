class Operation():
    def __init__(self, number1 = 0, number2 = 0):
        self.first = number1
        self.second = number2

    def get_numbers(self):
        return(f'Le premier nombre est {self.first}\nLe second nombre est {self.second}')

operation = Operation()
print(operation.get_numbers())