num = int(input('Digite um número inteiro: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')