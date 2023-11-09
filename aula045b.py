# Métodos de um conjunto

# .add()

flores_america = {'rosa', 'margarida', 'lirio', 'tulipa'}
flores_europa = {'rosa', 'lavanda', 'tulipa'}
print(flores_america)

flores_america.add('orquídea')  # .add() adiciona o item ao conjunto
print(flores_america)

# .diference()

print(flores_america.difference(flores_europa))  # Retorna um novo conjunto com itens do conjunto inicial que não estão
                                                 # nos outros conjuntos escolhidos


# .intersection()

print(flores_america.intersection(flores_europa))  # Retorna um novo conjunto com itens do conjunto inicial que também
                                                   # estão no outro conjunto escolhido


# .isdisjoint()

print(flores_america.isdisjoint(flores_europa))  # Retorna True se o conjunto inicial não tiver itens em comum com o
                                                 # conjunto escolhido. Conjuntos disjuntos não possuem itens em comum


# .issubset()

print(flores_america.issubset(flores_europa))  # Retorna True se todos os itens do conjunto inicial estão no outro
                                               # conjunto escolhido. Um conjunto é subconjunto de outro se todos seus
                                               # itens estão contidos no outro


# .issuperset()

print(flores_america.issuperset(flores_europa))  # Retorna True se cada elemento do conjunto parâmetro escolhido estão
                                                 # no conjunto inicial


# .pop()

flores_america.pop()   # Remove e retorna um item arbitrário do conjunto. Se o conjunto for vazio retorna um KeyError
print(flores_america)


# .symmetric_diference()

print(flores_america)
print(flores_europa)
print(flores_america.symmetric_difference(flores_europa))  # Retorna um conjunto com itens que estão em um dos
                                                           # conjuntos mas não no outro (ou exclusivo)


# .union()

print(flores_america.union(flores_europa))  # Retorna a união dos dois conjuntos


# .discard()

flores_america.discard('rosa')   # Retira o item do conjunto se ele estiver lá, se não tiver não acontece nada
print(flores_america)


# .clear()

flores_america.clear()  # Remove todos os elementos do conjunto
print(flores_america)

# .update()

flores_america.update(flores_europa)  # Atualiza o conjunto com todos os itens do outro conjunto
print(flores_america)
