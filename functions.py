#Function (de executar algo - [resumida]
#Funcao sempre precisa ser invocada
# def (Uso da palavra reservada que indica que é uma função)
# nome explicito e autoexplicativo
# sempre escrita em snake case
# o retorno é void (vazio)
def soma_dois_numeros(x:float, y:float):
    soma = x + y
    print("Resultado da soma é: ", soma)

# Subtrai dois numeros e retorna o valor
# o retorno é a subtração dos dois numeros
def subtrai_dois_numeros(x, y):
    subtracao = x - y
    return subtracao

soma_dois_numeros(10, 20)
subtracao = subtrai_dois_numeros(10, 20)
print("O valor da subtracao e: ", subtracao)

