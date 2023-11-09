# Tuplas são coleções parecidas com as listas, mas são limitadas por parênteses e são imutáveis

# Atribuição e tipo

montadoras = ("Ferrari", "Fiat", "Mercedes", "Renault")
print(montadoras)
print(type(montadoras))

tupla_vazia = ()
tupla_heterogenea = (2023, 11.58, montadoras, "pyPRO")
print(tupla_heterogenea)


# Operações Básicas

tupla1 = (2, 0, 1, 4)
tupla2 = (2, 0, 1, 9)

print(tupla1 + tupla2)   # Concatenação de duas tuplas
print(tupla1 * 3)        # Repete n vezes a tupla
print(tupla1 == tupla2)  # Verifica o valor-verdade
print(2 in tupla2)       # Verifica se o valor existe na tupla


# Função tuple()

navegadores = 'Vikings'
texto_para_tupla = tuple(navegadores)  # tuple() converte a informação em uma tupla
print(texto_para_tupla)

lista = [21, 43, 'Lucas', 'Y', 2.45]
lista_para_tupla = tuple(lista)
print(lista_para_tupla)

letras = ('a', 'b,', 'c')
numeros = (1, 2, 3)

tupla_aninhada = (letras, numeros)
print(tupla_aninhada)

# Indexação

cores = ('r', 'g', 'b', 'y', 'o', 'w')
print(cores[1:4])  # A indexação é semelhante a das listas
print(cores[:3])
print(cores[::2])
print(cores[::-1])

# Funções de tuplas

datas = (1982, 2002, 1986, 1978, 2003, 2009)

print(len(datas))  # Retorna o tamanho da tupla
print(sum(datas))  # Retorna a somatória dos elementos desde que sejam númericos
datas_organizadas = sorted(datas)  # Organiza os valores
print(datas_organizadas)


# Métodos de uma tupla

print(datas.count(2002))  # .count() retorna a quantidade de vezes que o item aparece na tupla
print(datas.index(2002))  # .index() retorna a posição que está o item
