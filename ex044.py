preco = float(input('Digite o valor da compra (R$) : '))
pgto = int(input("""1 - à vista (dinheiro/cheque) 
2 - à vista (cartão de crédito)
3 - em até 2x no cartão (sem juros)
4 - em 3x ou mais no cartão (com juros)
Selecione a forma de pagamento: """))

avista = preco - (preco * 10 / 100)
avistacartao = preco - (preco * 5 / 100)
parcelado3 = preco + (preco * 20 / 100)

if pgto == 1:
    print('Sua compra no valor de R${:.2f} vai custar R${:.2f} recebendo 10% de desconto por pagar á vista!'.format(preco, avista))
elif pgto == 2:
    print('Sua compra no valor de R${:.2f} vai custar R${:.2f} recebendo 5% de desconto por pagar á vista (no cartão)!'.format(preco, avistacartao))
elif pgto == 3:
    print('Sua compra no valor de R${:.2f} foi parcelada em 2x sem juros (no cartão)!')
elif pgto == 4:
    print('Sua compra no valor de R${:.2f} foi parcelada em 3x (no cartão), e vai custar R${:.2f} com 20% de juros!'.format(preco, parcelado3))