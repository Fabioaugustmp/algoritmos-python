class Car:

    #Construtor da classe
    def __init__(self, brand, model: str, year: int, color, name):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.name = name
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"The car {self.name} is running {self.is_running}"

    def stop(self):
        self.is_running = False
        return f"The car {self.name} has stopped {self.is_running}"

    #Função que descreve o meu carro
    def describe(self):
        return (f"The car {self.name} for brand {self.brand} of model {self.model}"
                f" from year {self.year} with color {self.color}")

    def __str__(self):
        return (f"The car {self.name} for brand {self.brand} of model {self.model}"
                f" from year {self.year} with color {self.color}")




