while True:
    n=int(input('Digite o ano de nascimento: '))
    c = 2020 - n
    f = 18 - c
    p = c - 18

    if c < 18:
        print('Você ainda não completou 18 anos, e ainda faltam {} anos para se alistar ao serviço militar.'.format(f))
    elif c == 18:
        print('Você tem 18 anos, portanto deve se alistar ao serviço militar.')
    elif c > 18:
        print('Você possui {} anos, e já se passaram {} anos desde o alistamento serviço militar.'.format(c ,p))
    else:
        print('Fim')
    r=str(input('Deseja tentar novamente? (s/n): ')).lower()
    if r !='s':
        break