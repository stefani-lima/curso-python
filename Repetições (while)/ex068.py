'''Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou.'''

from random import randint

soma = vitoria = 0

while True:
    num = int(input('Qual número você escolhe? '))
    computador = randint(0, 10)
    soma = num + computador
    print('-'*30)
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'O computador escolheu o número {computador}! A soma deu {soma}.')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        print('-' * 30)
        if soma % 2 == 0:
            vitoria += 1
            print('Você GANHOU!')
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        print('-' * 30)
        if soma % 2 == 1:
            vitoria += 1
            print('Você GANHOU!')
        else:
            print('Você PERDEU!')
            break
print('='*30)
print(f'Você venceu {vitoria} vezes consecutivas!')



