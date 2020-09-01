s=float(input('Digite o valor do seu salário: '))
r1=(s+s*10/100)
r2=(s+s*15/100)
if s >= 1250:
    print('O valor do seu salário era de R${} e recebeu um reajuste de 10%, portanto o valor reajustado é referente a importância de: R${}.'.format(s, r1))
else:
    print('O valor do seu salário era de R${} e recebeu um reajuste de 15%, portanto o valor reajustado é referente a importância de: R${}.'.format(s, r2))