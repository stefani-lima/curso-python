# Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número inteiro: '))
fatorial = 1
i = 1
while i <= num:
    fatorial *= i
    i += 1
print('O resultado do número escolhido em fatorial é: {}'.format(fatorial))