x: int
soma: int

x = float(input("Forneca o numero desejado: "))
soma = 0

#Executa enquanto a condição for verdadeira, para caso não seja e encerra o fluxo do loop
while x != 0:
    soma = soma + x
    x = float(input("Forneca o numero desejado: "))

print("SOMA = ", soma)