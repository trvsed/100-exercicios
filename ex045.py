from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print('POOH!!!\n')

print('-=' * 10)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')
