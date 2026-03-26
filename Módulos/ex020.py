''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação  de trabalhos  dos alunos.
Faça um programa que leia o nome dos quatro aluno e mostre a ordem sorteada. '''

from random import shuffle
aluno_1 = input('Digite o nome do aluno 1: ')
aluno_2 = input('Digite o nome do aluno 2: ')
aluno_3 = input('Digite o nome do aluno 3: ')
aluno_4 = input('Digite o nome do aluno 4: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista)
print('A ordem escolhida foi: {}!'.format(lista))