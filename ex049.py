while True:
    t=int(input('Digite um número para saber a sua tabuada: '))
    for c in range(1, 11):
        print('{} x {} = {}'.format(t, c, t*c))
    cont=str(input('Deseja continuar? (s/n): ')).lower()
    if cont !='s':
        break