# O escopo de uma variável é a amplitude ou o "hall" de atuação de uma variável,
# ou seja, até que parte do código aquele valor da variável é válido

# Existem variáveis do tipo "global" ou "local"

x = 0
y = 0  # Aqui a variável assume um escopo global

print("Y Global - ", y)
print("X Global - ", x)


def funcao():
    y = 4  # Aqui na função a variável possui um escopo local, prioritário dentro da função em relação ao global
    print("Y Local - ", y)
    print("X Local - ", x)  # O x não teve outro valor atribuído, assumindo seu valor global mesmo


funcao()
print("Y Global - ", y)
print("X Global - ", x)
