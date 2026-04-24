''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado.
O programa será interrompido quando o número solicitado for negativo.'''

cont = 1

while True:
    print('-'*30)
    num = int(input('Você deseja ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        print('Programa encerrado!')
        break
    for cont in range(1, 11):
        print(f'{num} X {cont} = {num*cont}')
        cont += 1

