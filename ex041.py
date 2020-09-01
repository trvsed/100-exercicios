idade = int(input('Digite o ano de nascimento do atleta: '))
base = 2020 - idade
if base <= 9:
    print('O atleta possui {} anos, portanto pertente a categoria MIRIM'.format(base))
elif base <= 14:
    print('O atleta possui {} anos, portanto pertence a categoria INFANTIL'.format(base))
elif base <= 19:
    print('O atleta possui {} anos, portanto pertence a categoria JUNIOR'.format(base))
elif base == 20:
    print('O atleta possui {} anos, portanto pertence a categoria SÊNIOR'.format(base))
else:
    print('O atleta possui {} anos, portanto pertence a categoria MASTER'.format(base))