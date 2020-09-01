valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor do seu salário? '))
anos = float(input('Em quantos anos você pretende pagar? '))
c1 = valor/anos
c2 = c1/12
c3 = c2*salario*30/100
if c2 > (salario*30/100):
    print('Seu financiamento foi negado pelo Banco')
else:
    print('Seu financiamento foi aprovado')

#Melhorar

