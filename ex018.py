from math import sqrt
x=float(input('Digite o valor do cateto oposto de um triângulo: '))
y=float(input('Digite o valor do cateto adjacente de um triângulo: '))
h=sqrt(x*x + y*y)
print('Com base no valor do comprimento do cateto oposto que é :{} em relação ao valor do cateto adjacente:{} o comprimento da hipotenusa é:{:.2f}'.format(x, y, h))