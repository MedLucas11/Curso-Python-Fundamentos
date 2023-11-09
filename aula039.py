# O comando "break" interrompe o looping de repetição
# O comando "continue" desvia o fluxo de execução para o topo do comando

n = 0
while True:
    print(f"O último valor de n é {n}.")    # Comando infinito
    n += 1
    if n > 5:
        break   # O break impede que o loop seja infinito e para a partir de n > 5


# Vamos fazer um comando parecido com o acima, mas que mostra apenas número ímpares, pulando os pares

n2 = 0
while True:
    if (n2 % 2) == 0:
        n2 += 1
        continue
    print(f"O último valor de n2 é {n2}")
    n2 += 1
    if n2 > 9:
        break
