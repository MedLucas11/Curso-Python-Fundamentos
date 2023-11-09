# Estrutura de repetição definida: Aquela que sabemos a quantidade de vezes que será repetida
# Um dos comandos utilizados para o loop é o "for".

soma = 0
for i in range(1, 6):
    idade = int(input(f"Entre com a idade {i}: "))  # Para adicionar uma variável no comando "input", utilizar a
    soma = soma + idade                             # formatação da string (f"") e a variável entre chaves.
media = soma/5
print("A média das idades é: ", media)
