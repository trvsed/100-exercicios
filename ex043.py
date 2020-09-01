while True:
    peso = float(input('Qual é seu peso? (Kg): '))
    alt = float(input('Qual é sua altura? (m) '))
    imc = peso/alt ** 2
    if imc <= 18.5:
        print('Seu IMC em relação ao seu peso e altura é {:.1f}\nMelhor sua alimentação, seu IMC indica baixo peso!'.format(imc))
    elif imc <= 25:
        print('Seu IMC em relação ao seu peso e altura é {:.1f}\nParabéns, você está no peso ideal!'.format(imc))
    elif imc <= 30:
        print('Seu IMC em relação ao seu peso e altura é {:.1f}\nComece a treinar, seu IMC indica sobrepeso!'.format(imc))
    elif imc <= 40:
        print('Seu IMC em relação ao seu peso e altura é {:.1f}\nVá para a academia, seu IMC indica obesidade!'.format(imc))
    elif imc >= 40:
        print('Seu IMC em relação ao seu peso e altura é {:.1f}\nProcure um médico, seu IMC indica obesidade mórbida!'.format(imc))

    cont=str(input('Deseja continuar? (s/n): ')).lower()
    if cont == 's':
        continue
    elif cont == 'n':
        break
    else:
        print('Opção Inválida!')
        break
