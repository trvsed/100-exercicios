frase=str(input('Digite uma frase: ')) .upper() .strip()
A1 = frase.count('A')
AP = frase.find('A')+1
AU = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase.'.format(A1))
print('A primeira letra A apareceu na posição {}'.format(AP))
print('A última letra A apareceu na posição {}'.format(AU))