# Funções com parâmetro

def area_circulo(raio):
    pi = 3.141592
    area = pi * pow(raio, 2)
    return area


def area_cilindro(raio, altura):
    area = area_circulo(raio) * altura
    return area


r = float(input('Digite o valor do raio do cilindro: '))
h = float(input('Digite a altura do cilindro: '))
a = area_cilindro(r, h)
print(f'O valor da área do cilindro de raio {r} e altura {h} é igual a {a}')
