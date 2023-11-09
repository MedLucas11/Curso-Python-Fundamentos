# Dicionários

# Dicionários são coleções de um conjunto de pares chave:valor, com uma restrição de que a chave seja única dentro da
# coleção

# Os dicionários são construídos utilizando chaves {}
# Utiliza-se ':' para separar a chave do valor
# Sempre o operador a esquerda é a chave, e o da direita o valor
# Os dicionários são indexados pela chave
# As chaves são "case sensitive" (Maiúsculas e minúsculas importam)


# Atribuição e tipo

f1 = {1: 'Mercedes', 2: 'Ferrari', 3: 'Renault'}
dic_vazio = {}
dic_heterogeneo = {1: 45, 'a': 'amor', 3.14: 'pi', 'litros': 2}
print(f1)
print(type(f1))
print(type(dic_heterogeneo))

# Operações Básicas

print(f1 == dic_heterogeneo)  # Única operação de um dicionário é a comparação

# Função dict()

numeros = dict(um=1, dois=2, tres=3)  # Podemos usar dict() passando uma lista de argumentos válidos
print(numeros)

dic1 = dict([('ana', 341), ('pedro', 3453), ('marcio', 8988)])  # Podemos também passar um iterável para montar o dict
print(dic1)

# Indexação e alteração

print(dic1['ana'])  # Passar a chave retorna o valor associado a ela

dic1['lucas'] = 21  # Ao não encontrar a chave ele automaticamente cria uma com este valor correspondente
print(dic1)

# Funções built-ins

print(len(dic1))  # Retorna o número de duplas (chave:valor) do dicionário
print(all(dic1))  # Retorna True se todos os valores das CHAVES dicionário forem verdadeiros (!=0)
print(any(dic1))  # Retorna True se algum dos valores das CHAVES do dicionário for verdadeiro

valores_ordenado = sorted(dic1)  # Irá organizar o dicionário e retornar uma LISTA, mantendo o dict intacto
chaves_ordenadas = sorted(dic1.values())
dicionario_ordenado = sorted(dic1.items())
print(valores_ordenado)
print(chaves_ordenadas)
print(dicionario_ordenado)
