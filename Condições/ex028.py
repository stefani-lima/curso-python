# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.

import random
num = random.randint(0, 5)
tentativa = int(input('Tente acertar o número escolhido de 0 a 5: '))
if tentativa == num:
    print('Parabéns, você acertou!')
else:
    print('Tente novamente!')
print('O número escolhido pelo computador foi: {}'.format(num))
