# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ela.

texto = input('Digite algo: ')
print('O tipo primitivo é {}'.format(type(texto)))
print('É alfanumérico?', texto.isalnum())
print('É numérico?', texto.isnumeric())
print('Está em maiúsculo?', texto.isupper())
