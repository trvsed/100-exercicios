c1 = 0
c2 = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        c1 += 1
        c2 += c
print('{} números são impares num total de 500, a soma de todos esses valores é de: {}'.format(c1, c2))