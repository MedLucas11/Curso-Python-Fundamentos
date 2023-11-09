# Métodos de uma lista

cidades = ['Sorocaba', 'São Paulo', 'Rio de Janeiro', 'New York']
print(cidades)

cidades.append('Oslo')  # .append() adiciona o parâmetro ao fim da lista
print(cidades)

print(cidades.count("São Paulo"))  # .count() conta quantas vezes o item aparece na lista
print(cidades.count("Itu"))

cidades.insert(2, 'Itu')  # .insert() adiciona um parâmetro no índice indicado, deslocando o resto da lista para direita
print(cidades)

print(cidades.index("São Paulo"))  # .index() retorna o índice (posição) em que se encontra o parâmetro

cidades2 = ['Miami', 'Tokyo', 'La Paz']
cidades.extend(cidades2)   # .extend() adiciona os itens de uma lista a outra
print(cidades)

cidades.remove('Itu')  # .remove() remove a primeira ocorrência do parâmetro na lista
print(cidades)

cidades.sort()  # .sort() ordena e modifica a própria lista, sem criar uma cópia como o sorted()
print(cidades)

cidades.reverse()  # .reverse() inverte a ordem da lista
print(cidades)

cidades.pop(0)  # .pop() remove o item indicado pelo índice, se este for omitido irá remover o item mais a direita
cidades.pop()
print(cidades)
