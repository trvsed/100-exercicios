s = 0
v = 0
for c in range(1, 7):
    n=int(input('Digite o {} valor: '.format(c)))
    if n % 2 ==0:
        s += 1
        v += n
print('Você informou {} número(s) pares e a soma foi {}!'.format(s, v))
