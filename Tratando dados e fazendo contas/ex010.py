# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

saldo = (float(input('Digite o seu saldo atual: R$ ')))
if saldo > 0:
    print('Com seu saldo atual de R$ {:.2f}, você conseguirá comprar {:.2f} dólares.'.format(saldo, saldo / 5.20))
else:
    print('Com seu saldo atual de R$ {:.2f}, não é possível comprar dólar'.format(saldo))