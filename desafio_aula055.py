def primo(numero):
    if numero == 2:
        return True
    elif numero > 2:
        d = 2
        while d < n:
            if numero % d == 0:
                d += 1
                return False
            else:
                return True


n = int(input('Digite um número para saber se ele é primo: '))

if primo(n):
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')
