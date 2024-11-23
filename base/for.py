x: int
soma: int

N = int(input("Quantos numeros serão digitados? "))
soma = 0
for i in range(0, N):
    x = float(input("Digite o numero: "))
    soma = soma + x

print(f"A soma das {N} iterações foi = {soma}")