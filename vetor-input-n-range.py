# int(alguma coisa) -> Casting
N = int(input("Quantos numeros deseja adicionar? "))

#Definiu um tamanho para o meu vetor
vet = []

for i in range(1, N):
    vet[i] = float(input("Informe o valor desejado: "))

print()
print("=== VALORES INFORMADOS ===")

for j in range(0, len(vet)):
    print(f"{j} - N: {vet[j]}")




