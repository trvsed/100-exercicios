media1 = float(input('Digite o valor da primeira nota: '))
media2 = float(input('Digite o valor da segunda nota: '))
mediaFinal = media1+media2/2
if mediaFinal < 5.0:
    print('Sua média foi {} portanto você está reprovado.'.format(mediaFinal))
elif mediaFinal >= 5.0 and mediaFinal < 7:
    print('Sua média foi {} portanto você está em recuperação.'.format(mediaFinal))
elif mediaFinal >= 7.0:
    print('Sua média foi {} portanto você está aprovado, parabéns!!!'.format(mediaFinal))