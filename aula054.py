# Argumentos *args e **kwargs

# Utilizamos *args e **kwargs quando não sabemos a quantidade de parâmetros a serem passados

def soma(*args):
    print(args)
    total = sum(args)
    return total


print(soma(1, 2, 3, 4, 5))  # Quando utilizamos *args podemos passar quantos valores de parâmetro quisermos, que serão
                            # transformados em uma tupla


# **kwargs
# Nesse caso ele irá receber um dicionário

def comida_favorita(**kwargs):
    print(kwargs)
    for chave in kwargs:
        print(f'{chave} gosta de {kwargs[chave]}')


comida_favorita(ana='bacalhoada', marcelo='risoto', adriana='camarão')
