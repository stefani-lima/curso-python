''' Crie um programa que leia vários números inteiros pelo teclado.
No final, mostre: média dos valores, maior e menos números lidos.
O programa deverá perguntar se o usuário quer ou não continuar.'''

soma = maior = menor = media = cont = 0
frase = 'S'
while frase in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    frase = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if maior < num:
        maior = num
    else:
        menor = num
media = soma / cont
print('A média dos valores é: {}'.format(media))
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))