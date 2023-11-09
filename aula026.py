# O tipo de dado 'string' é uma sequência de caracteres, escrito entre aspas simples ou duplas

nome = 'Lucas'
letra = 'a'
letra2 = "b"

print(nome, letra, letra2)
print(type(nome))

# Podemos inserir uma quebra de linha para escrever em mais de uma linha, utilizando 3 aspas

frase = '''Batatinha quando "nasce",
espalha a rama pelo chão'''
print(frase)

# Por se tratar de uma sequência de caracteres, uma string é como uma 'lista'
# e cada caractere é associado a uma posição

print(frase[0])

# Com esse recurso podemos fazer o 'slice' ou 'recorte' da string

print(frase[0:1:1])
# 1º parâmetro --> início
# 2º parâmetro --> limite superior (pegará os valores até a posição n-1)
# 3º parâmetro --> tamanho do passo (quanto vai "andar" a cada passo, deixando em branco será 1)

print(frase[0:9])
print(frase[10:16])
print(frase[0:9:2])

# Podemos utilizar também valores negativos no passo para fazer o caminho inverso

print(frase[::-1])  # Deixando os 2 primeiros parâmetros em branco irá percorrer toda a string

# Outra operação importante é o 'strip', que vai "limpar" os espaços em branco a esquerda e a direita

palavra = '   pyPRO   '
print(palavra)
print(palavra.strip())

palavra2 = 'Lucas'
print(palavra, palavra2)
print(palavra.strip(), palavra2)

# Existe uma função que coloca todas as letras para maiúsculo ou minúsculo

print(palavra.upper())
print(palavra.lower())

# Podemos separar uma frase, por exemplo, utilizando o split(), que cria uma lista com cada parte da frase

frase2 = "Batatinha quando nasce"
print(frase2.split())  # Se não passar nenhum parâmetro para o split() ele irá separar baseado nos espaços

email = 'medlucas@hotmail.com'
print(email.split('@'))  # Utilizando o parâmetro '@' irá separar o email antes e depois do arroba
