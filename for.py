x: int
soma: float = 0

N = int(input("Quantos numeros deseja adicionar? "))
for i in range(0, N):
    x = float(input("Digite o numero a ser somado: "))
    soma = soma + x

print(f"A soma dos {N} numeros e igual {soma}")