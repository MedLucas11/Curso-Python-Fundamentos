nomes = []
nomes_idades = {}
nomes_calcados = {}

for i in range(1, 6):
    nome = input(f"Digite o nome {i}: ")
    nomes.append(nome)
    idade = int(input(f"Digite a idade {i}: "))
    numero = int(input(f"Digite o número de calçado {i}: "))
    nomes_idades.setdefault(nome, idade)
    nomes_calcados.setdefault(nome, numero)

nomes_ordenados = sorted(nomes)
nomes_idades_ordenados = dict(sorted(nomes_idades.items()))
idades_ordenadas = list(nomes_idades_ordenados.values())
nomes_calcados_ordenados = dict(sorted(nomes_calcados.items()))
calcados_ordenados = list(nomes_calcados_ordenados.values())

for (n, i, c) in zip(nomes_ordenados, idades_ordenadas, calcados_ordenados):
    print(f"Nome: {n}, Idade: {i}, Número de Calçado: {c}")

soma_idades = sum(idades_ordenadas)
qtd_idades = len(idades_ordenadas)
soma_calcados = sum(calcados_ordenados)
qtd_calcados = len(calcados_ordenados)
media_idade = soma_idades / qtd_idades
media_calcados = soma_calcados / qtd_calcados

print(f"A média de todas as idades é {media_idade} e a média dos números de calçado é {int(media_calcados)}")
