pesos=[]
for c in range (1, 6):
    valor=float(input('Digite o valor do {}º peso: '.format(c)))
    pesos+=[valor]
print('O maior peso é {}'.format(max(pesos)))
print('O menor peso é {}'.format(min(pesos)))
