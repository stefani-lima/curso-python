# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -> 1 para binário
# -> 2 para octal
# -> 3 para hexadecimal

num = int(input('Escreva um número: '))
base_conversao = int(input('Escolha qual será a base de conversão: -> 1 para binário, 2 para octal e 3 para hexadecimal: '))

if base_conversao == 1:
    print('{} convertido para Binário é: {}'.format(num,(bin(num))))
elif base_conversao == 2:
    print('{} convertido para Octal é: {}'.format(num, (oct(num))))
elif base_conversao == 3:
    print('{} convertido para Hexadecimal é: {}'.format(num, (hex(num))))
else:
    print('O número que você escolheu para a base de conversão não é válido, tente novamente!')