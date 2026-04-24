''' Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos. '''

a = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
termo = a
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')