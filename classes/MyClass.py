class MyClass:
    #Atributo
    name = "I am class"

    #Construtor da minha classe com (N) parametros da minha classe
    def __init__(self, name):
        self.name = name

    #Uma função que diz qual é o meu nome
    def my_name(self):
        return f"My name is: {self.name}"

################################################

#Instancia de Classe
firstClass = MyClass("Fabio")
secondClass = MyClass("Diogo")

#Invocando ou Chamando a funcao da minha classe
print(firstClass.my_name())
print(secondClass.my_name())



