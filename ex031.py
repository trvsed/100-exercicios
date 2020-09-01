d=float(input('Digite a distância em Km da sua viagem: '))
p1=(d*0.50)
p2=(d*0.45)
if d <= 200:
    print('O valor total da sua viagem custará: {}'.format(p1))
else:
    print('O valor total da sua viagem custará: {}'.format(p2))
