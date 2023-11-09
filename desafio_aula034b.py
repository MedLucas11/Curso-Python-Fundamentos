sexo = input("Digite M para masculino ou F para feminino: ")
if sexo != 'M' or sexo != 'F':
    print("Entrada errada, digite M ou F")

altura = float(input("Digite sua altura em metros: "))

if sexo == 'M':
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é", peso, "kg")
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é", peso, "kg")
