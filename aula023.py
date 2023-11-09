# O tipo inteiro (int) são basicamente os números inteiros

print(type(10))

# Podemos associar inteiros a uma variável

num = 10
print(num)

# A informação do tipo inteiro é guardada em um objeto, por isso a alocação de memória não é fixa, sendo alocado
# dinamicamente
# Por isso não existe limite para os números guardado na linguagem python

numero_muito_grande = 2**2000
print(numero_muito_grande)

# Podemos representar casas das centenas com underline (_) para facilitar na visualização

um_milhao = 1_000_000
print(um_milhao)

# Podemos fazer algumas operações da seguinte forma também:

num = num+1
print(num)

# Com o comando dir() podemos verificar todas as possíveis utilizações com a classe int

print(dir(num))
