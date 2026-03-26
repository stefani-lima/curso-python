# Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome do escolhido.

from random import choice
aluno_1 = input('Digite o nome do aluno 1: ')
aluno_2 = input('Digite o nome do aluno 2: ')
aluno_3 = input('Digite o nome do aluno 3: ')
aluno_4 = input('Digite o nome do aluno 4: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
print('O aluno escolhido foi: {}!'.format(choice(lista)))
