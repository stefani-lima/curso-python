# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um valor: '))
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))