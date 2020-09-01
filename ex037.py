num=int(input('Digite um número qualquer: '))
base=int(input('Escolha uma base de conversão:\n1 para binário;\n2 para octal;\n3 para hexadecimal.\nDigite o valor: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if base == 1:
    print('A base {} convertida para binário é: {}'.format(num, binario[2:]))
elif base == 2:
    print('A base {} convertida para octal é: {}'.format(num, octal[2:]))
elif base == 3:
    print('A base {} convertida para hexadecimal é {}'.format(num, hexadecimal[2:]))
else:
    print('A base escolhida não é válida.')