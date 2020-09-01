from time import sleep
start=str(input('Digite "começar" sem aspas para iniciar a contagem: ')).lower() .strip()
if start == 'começar':
    for c in range(10, -1,-1):
        print(c)
        sleep(1)
    print('Feliz ano novo!!!')
else:
    print('Entrada Inválida!')