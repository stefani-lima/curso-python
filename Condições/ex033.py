# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Digite três números. ')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
if (num1 > num2) and (num2 > num3):
    print('A ordem correta do maior para o menor é: {}, {}, {}'.format(num1, num2, num3))
elif (num1 > num2) and (num3 > num2):
    print('A ordem correta do maior para o menor é: {}, {}, {}'.format(num1, num3, num2))
elif (num2 > num1) and (num1 > num3):
    print('A ordem correta do maior para o menor é: {}, {}, {}'.format(num2, num1, num3))
elif (num2 > num3) and (num3 > num1):
    print('A ordem correta do maior para o menor é: {}, {}, {}'.format(num2, num3, num1))
elif (num3 > num1) and (num1 > num2):
    print('A ordem correta do maior para o menor é: {}, {}, {}'.format(num3, num1, num2))
else:
    print('A ordem correta do maior para o menor é: {}, {}, {}'.format(num3, num2, num1))





