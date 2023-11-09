# Sets são coleções não ordenadas (sem índice) que não permitem a duplicação de elementos
# Os conjuntos são delimitados utilizando chaves {}
# Os conjuntos suportam operações matemáticas de união, intersecção, diferença e diferença simétrica
# Os sets são estruturas MUTÁVEIS


# Atribuição e tipo

peixes = {'tubarão', 'baleia', 'atum', 'sardinha', 'tubarão'}
numeros = {1, 2, 3, 6, 9, 23, 67}
mix = {1, 'a', 'Lucas', 3.56, (2, 4, 5)}

print(peixes)
print(type(peixes))
print(numeros)
print(mix)

# Função set()

a = set("abracadabra")    # Cria o set e elimina as repetições
print(a)

b = set('alacazam')
print(b)


# Operadores

print(a | b)  # O pipe "|" representa a união dos dois conjuntos
print(a & b)  # O "%" representa a intersecção dos conjuntos
print(a ^ b)  # O "^" representa a diferença entre os conjuntos, ou seja, o que eles têm de diferente
print(a - b)  # O "-" representa a diferença simétrica entre os conjuntos, ou seja, o que tem no 'a' que não tem no 'b'


# Funções built-ins

flores_europa = {'rosa', 'lavanda', 'tulipa'}
flores_america = {'rosa', 'tulipa', 'lirio', 'margarida'}

print(len(flores_europa))   # len() retorna o tamanho do conjunto
print(sorted(flores_europa))  # sorted() retorna uma LISTA ordenada do conjunto

