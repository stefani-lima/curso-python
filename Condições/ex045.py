# Crie um programa que faça o computador jogar jokenpô com você.

import random
jokenpo = str(input('Vamos jogar! Pedra, papel ou tesoura? ')).upper().strip()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = random.choice(lista)

if escolha == 'PEDRA' and jokenpo == 'PEDRA':
    print('Pedra!')
    print('Empate, vamos de novo!')
elif escolha == 'PEDRA' and jokenpo == 'PAPEL':
    print('Pedra!')
    print('Você ganhou! :(')
elif escolha == 'PEDRA' and jokenpo == 'TESOURA':
    print('Pedra!')
    print('Ganhei!')
elif escolha == 'PAPEL' and jokenpo == 'PAPEL':
    print('Papel!')
    print('Empate, vamos de novo!')
elif escolha == 'PAPEL' and jokenpo == 'PEDRA':
    print('Papel!')
    print('Ganhei!')
elif escolha == 'PAPEL' and jokenpo == 'TESOURA':
    print('Papel!')
    print('Você ganhou! :(')
elif escolha == 'TESOURA' and jokenpo == 'TESOURA':
    print('Tesoura!')
    print('Empate, vamos de novo!')
elif escolha == 'TESOURA' and jokenpo == 'PEDRA':
    print('Tesoura!')
    print('Você ganhou! :(')
elif escolha == 'TESOURA' and jokenpo == 'PAPEL':
    print('Tesoura!')
    print('Ganhei!')

