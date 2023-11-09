# Outro comando utilizado para loops é o "while", sendo mais utilizado em estruturas indefinidas
# Estrutura indefinida: Não sabemos a quantidade de vezes que a ação será repetida

idade = 0
soma = 0
quantidade = 0

while idade != 1000:
    idade = int(input(f"Digite a idade {quantidade + 1}: "))
    if idade != 1000:
        soma += idade  # soma = soma + idade
        quantidade += 1

if quantidade == 0:
    print("Não foi digitada uma quantidade válida de idades.")
else:
    media = soma / quantidade
    print(f"A medias das {quantidade} idades é: {media}.")
