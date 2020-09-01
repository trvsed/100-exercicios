from math import cos, sin, tan, radians
a=int(input('Digite o valor de um ângulo: '))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O ângulo de: {}º, tem o valor de seno referente a: {:.3f}, cosseno referente a: {:.3f} e tangente referente a: {:.3f}'.format(a, s, c, t))