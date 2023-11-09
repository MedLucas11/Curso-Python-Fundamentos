# Funções com parâmetro padrão

# Podemos passar um valor padrão para os parâmetros, que será utilizado caso o parâmetro seja omitido na chamada

def potencia(numero, expoente=2):           # Se o expoente for omitido, será utilizado o 2
    resultado = pow(numero, expoente)
    return resultado


n = float(input('Digite o número: '))
e = int(input('Digite o expoente: '))

print(f'Valor da potência utilizando o expoente: {potencia(n, e)}')
print(f'Valor da potência sem utilizar o expoente: {potencia(n)}')


# Parâmetros nomeados

print(f'Valor da potência utilizando o expoente: {potencia(expoente=e, numero=n)}')   # Nomeando os parâmetros
                                                                                      # podemos inverter sua chamada
