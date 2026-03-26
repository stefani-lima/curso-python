''' Crie um programa que leia o nome completo de uma pessoa e mostre:
 -> O nome com todas as letras maiúsculas
 -> O nome com todas as letras minúsculas
 -> Quantas letras ao todos (sem contar espaços)
 -> Quantas letras tem o primeiro nome '''

from os.path import split

nome = input('Digite seu nome completo: ')

print('Seu nome com todas as letras maiúsculas:', nome.upper())
print('Seu nome com todas as letras minúsculas:', nome.lower())
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format((nome.find(' '))))
