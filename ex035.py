c1=int(input('Digite o comprimento da primeira reta: '))
c2=int(input('Digite o comprimento da segunda reta: '))
c3=int(input('Digite o comprimento da terceira reta: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print ('A soma das três retas são iguais, portanto elas formam um triângulo.')
else:
    print('A soma das três retas são diferentes, portanto não formam um triângulo.')