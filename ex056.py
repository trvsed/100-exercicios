somaIdades = 0
sexoM = []
sexoF = []
idadeM = []
idadeF = []
nomeMV = ''
for c in range (1, 5):
    nome=str(input('Digite o seu nome: ')).capitalize()
    idade=int(input('Digite a sua idade: '))
    if idade:
        somaIdades += idade
    mediaIdade = somaIdades/4
    sexo=str(input('Qual é o seu sexo? (f/m): ')).lower()
    if sexo == 'm':
        sexoM += sexo
        idadeM += idade
        if idade > idade:
            nomeMV += nome
    elif sexo == 'f':
        sexoF += sexo
        idadeF += idade
        print('A média das idades no grupo é de: {:.0f} anos'.format(mediaIdade))
        print('O homem mais velho grupo tem {} anos e se chama {}'.format(max(idadeM), nomeMV))