a = int(input('Digite o primeiro número: '))
b = int(input('Digite um segundo número: '))
c = int(input('Digite um terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi {}.'.format(menor))
print('O maior número digitado foi {}.'.format(maior))