# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Você está acima do limite de velocidade! Você foi multado no valor de R$ {}.'.format((velocidade - 80) * 7))
else:
    print('Você está dentro da velocidade permitida!')
