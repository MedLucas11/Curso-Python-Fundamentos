numero = int(input("Digite um número: "))
soma = 0
resto = 0

while numero != 0:
    resta = numero % 10
    soma += resta
    numero = int(numero / 10)

print(f"A soma é igual a {soma}")
