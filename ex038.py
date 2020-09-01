while True:
    num1=int(input('Digite o primeiro valor: '))
    num2=int(input('Digite o segundo valor: '))
    if num1 > num2:
        print('Entre os valores digitados, o maior foi {} e o menor {}.'.format(num1, num2))
    elif num1 < num2:
        print('Entre os valores digitados, o maior foi {} e o menor {}.'.format(num2, num1))
    else:
        print('Ambos os valores são iguais.')
        resp=str(input('Deseja tentar novamente? (s/n): ')).lower()
        if resp !='s':
            break
