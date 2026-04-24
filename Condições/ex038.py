# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
# -> O primeiro valor é maior
# -> O segundo valor é maior
# -> Não existe valor maior, pois os dois são iguais

print('Escreva dois números.')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
if num1 > num2:
    print('O primeiro valor ({}) é maior que ({})!'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor ({}) é maior que ({})!'.format(num2, num1))
else:
    print('Não existe valor maior, pois os dois são iguais!')