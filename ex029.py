v=int(input('Qual a sua velocidade? '))
m = (v * 7) - 560
if v > 80:
    print('Você ultrapassou o limite de velocidade de 80km, e será multado!\n A multa aplicada é de R$7.00 por cada km excedido, num total de R${}!'.format(m))
else:
    print('Você não ultrapassou o limite de velocidade de 80km, e não será multado!')