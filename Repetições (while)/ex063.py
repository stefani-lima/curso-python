''' Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. '''

n = int(input('Quantos elementos você quer mostrar? '))
num1 = 0
num2 = 1
print('{} -> {} -> '.format(num1, num2), end='')
cont = 3
while cont <= n:
    cont += 1
    num3 = num1 + num2
    print('{} ->'.format(num3), end='')
    num1 = num2
    num2 = num3
print('FIM')


