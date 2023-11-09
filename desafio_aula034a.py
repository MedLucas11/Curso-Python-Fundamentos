n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("Entrada errada, digite um número positivo")
else:
    if (n % 2) == 0:
        print(n, "é um número par!")
    else:
        print(n, "é um número ímpar!")
