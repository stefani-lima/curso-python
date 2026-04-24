''' Melhore o desafio 028. Agora o jogador vai tentar adivinhar até acertar, mostrando quantos palpites foram necessários.
Desafio 028:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
 descobrir qual foi o número escolhido pelo computador. '''

import random
from random import randint

num = random.randint(0, 10)
num_tentativa = 0
while True:
    num_tentativa += 1
    tentativa = int(input('Tente acertar o número escolhido de 0 a 10: '))
    if tentativa != num:
        print('Tente novamente!')
    else:
        print('Parabéns, você acertou!')
        print('Você precisou de {} tentativas.'.format(num_tentativa))
        break
print('O número escolhido pelo computador foi: {}'.format(num))