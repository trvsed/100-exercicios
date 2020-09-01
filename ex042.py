lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar um triângulo!', end='\n')

    if lado1 == lado2 and lado2 == lado3:
        print('De acordo com a medida das retas {}x{}x{}, é um triângulo Equilátero.'.format(lado1, lado2, lado3))

    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('De acordo com a medida das retas {}x{}x{}, é um triângulo Isósceles.'.format(lado1, lado2, lado3))

    elif lado1 != lado2 != lado3 != lado1:
        print('De acordo com a medida das retas {}x{}x{}, é um triângulo Escaleno.'.format(lado1, lado2, lado3))

else:
    print('A soma das três retas são diferentes, portanto não formam um triângulo.')