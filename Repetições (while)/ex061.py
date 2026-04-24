''' Refaça o desafio 051, usando a estrutura while. Desafio 051:

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. '''

a = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
termo = a
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')
