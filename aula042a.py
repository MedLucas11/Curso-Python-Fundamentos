# Lista são coleções (caracteres, strings, números...) ordenados, separados por vírgula e entre colchetes

# Listas Homogêneas: [1, 2, 3] ; ['a', 'b', 'c'] ; ['texto1', 'texto2']
# Listas Heterogêneas: [1, 'a', 'texto1', [1, 2, 3], 345, ...]

# Atribuição e tipo:

lista_de_numeros = [1, 2, 5, 6, 2, 6, 43]
print(type(lista_de_numeros))
print(dir(lista_de_numeros))

lista_heterogenea = [25, 65.13, 'cachorro', True, 'A', [1, 2, 3]]
lista_vazia = []

# Operações básicas:

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]

print(lista1 + lista2)    # Concatenação das listas
print(lista1 * 3)         # Exibe n vezes a lista
print(lista1 == lista2)   # É possível comparar os valores das listas
print(5 in lista1)        # O comando "in" verifica se o valor está na lista

# Função list()

frase = "Um texto qualquer"

lista_caracteres = list(frase)  # Transforma o parâmetro em uma lista
print(lista_caracteres)

lista_letras = ['a', 'b', 'c']
print(lista_letras + list(frase))

# Indexação e fatiamento de listas

print(lista1[0])  # Os valores da lista começam no 0
print(lista_caracteres[3])
print(lista1[-2])  # Um número negativo no índice percorre a lista no sentido inverso

print(lista1[0:2])   # Podemos fatiar a lista nos elementos desejados
print(lista_caracteres[0::2])


# Modificação de itens de uma lista

lista1[0] = 10  # Substitui o elemento do índice
print(lista1)

lista3 = lista1   # Os elementos de ambas listas estão no mesmo espaço de memória, se um é alterado o outro também é
lista3[0] = 5
print(lista3, lista1)

# Funções e built-ins

print(len(lista1))  # len() retorna o tamanho da lista
print(sum(lista1))  # sum() soma os números de uma lista

lista_logica = [True, False, False, True]
lista_logica2 = [0, 0, 1, 0, 1, 0]     # Podemos utilizar 0 como valor lógico "False"
print(any(lista_logica), any(lista_logica2))   # any() retorna True se tiver algum valor True na lista
print(all(lista_logica), all(lista_logica2))   # all() retorna True se todos os valores da lista forem True

lista_numeros = [3, 7, 1, 2, 7, 9, 4, 8, 6]
lista_ordenada = sorted(lista_numeros)

print(lista_numeros)
print(lista_ordenada)
