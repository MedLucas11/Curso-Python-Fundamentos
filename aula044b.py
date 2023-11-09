# Métodos de um dicionário

filmes = {'avatar': 2009, 'titanic': 1997, 'star wars': 2015, 'harry potter': 2011, 'avengers': 2012}
print(filmes)

# .clear()

filmes.clear()  # Limpa totalmente o dicionário
print(filmes)
filmes = {'avatar': 2009, 'titanic': 1997, 'star wars': 2015, 'harry potter': 2011, 'avengers': 2012}

# .fromkeys()

filmes_novo = filmes.fromkeys(filmes)   # Cria um dicionário com as chaves do original
print(filmes_novo)

filmes_novo = filmes.fromkeys(filmes, 2013)   # Posso passar um valor Default para todas as chaves
print(filmes_novo)

# .get()

print(filmes.get('frozen'))        # Retorna o valor da chave especificada, se não tiver um valor retorna o valor
print(filmes.get('frozen', 2013))  # padrão ou None
print(filmes.get('avatar'))

# .items(), .keys() e .values()

print(filmes.items())   # Retorna os itens do dicionário como uma lista de tuplas
print(filmes.values())  # Retorna apenas os valores do dicionário como uma lista
print(filmes.keys())    # Retorna apenas as chaves do dicionário como uma lista

# .update()

filmes.update({'frozen': 2013})  # Adiciona o item ao fim dicionário
print(filmes)

# .setdefault()

filmes.setdefault('minions')  # Insere a chave no dicionário com o valor None se não for especificado
print(filmes)
filmes.setdefault('ironman', 2013)  # Insere a chave com o valor especificado e retorna o valor
print(filmes)
print(filmes.setdefault('ironman', 2013))

# .pop()

filmes.pop("minions")  # Remove a chave especificada e retorna o seu valor
print(filmes)

# .popitem()

filmes.popitem()   # Irá retirar o último item do dicionário e retornar sua tupla
print(filmes)
