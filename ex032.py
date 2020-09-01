while True:
    a=int(input('Digite um ano: '))
    num = a % 4
    if num == 0:
        print('{} é um ano bissexto!'.format(a))
    else:
        print('{} não é um ano bissexto!'.format(a))
    cont=str(input('Deseja descobrir se outro ano é bissexto? (s/n): ')) .lower()
    if cont!='s':
        break
