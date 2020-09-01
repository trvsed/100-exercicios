from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range (1, 7+1):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
        print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
        print('E também tivemos {} pessoas menores de idade'.format(menores))