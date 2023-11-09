# Os números decimais são do tipo 'float', ou seja, de ponto flutuante

x = 10.0
print(type(x))

# Em ponto flutuante há uma limitação na questão do tamanho do número, sendo o limite o seguinte:

print(2.45**792)

# Aqui também é possível utilizar o underline (_) para separar casas de milhar

y = 1_000_000.000_100_100
print(y)

# Os números complexos em python são acompanhados por "j"

complexo = 5j
print(type(complexo))
