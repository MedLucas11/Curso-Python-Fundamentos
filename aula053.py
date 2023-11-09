# Documentação de funções: DocString

# A documentação é muito útil para exemplificar o que estava sendo implementado com determinada função, auxiliando
# na leitura do código posteriormente, seja para você msm ou para sua equipe

def potencia(numero, expoente=2):
    """Função que calcula a potência de um número
    Valor de Entrada:
    numero - número a ser calculado (float)
    expoente - expoente a ser utilizado (int)

    Resultado:
    Resultado do cálculo da potência (float)"""
    resultado = pow(numero, expoente)
    return resultado


n = float(input('Digite o número: '))
e = int(input('Digite o expoente: '))

print(f'Valor da potência utilizando o expoente: {potencia(n, e)}')
print(f'Valor da potência sem utilizar o expoente: {potencia(n)}')
print('-------------------------------------------------------------')
help(potencia)
