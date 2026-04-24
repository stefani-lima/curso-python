# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Escreva um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
if tot == 2:
    print('Esse valor é primo!')
else:
    print('Esse valor não é primo!')