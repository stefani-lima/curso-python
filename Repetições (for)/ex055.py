# Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

for i in range (1, 5+1):
    peso = float(input('Peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))


