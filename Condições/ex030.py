# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar.

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))