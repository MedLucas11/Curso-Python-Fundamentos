# Funções com retorno

def um_megabit():
    valor = 1024 * 1024
    return valor


def um_megabit_alternativa():
    return 1024 * 1024


x = um_megabit()
y = um_megabit_alternativa()
print(f'O total de bits é {x}')
print(f'O total de bits é {y}')
