# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram entre 1 e 500.

soma = 0
i = 0
for i in range (1, 500+1, 2):
    if i % 3 == 0:
        soma += i
        i = i + 1
print('A soma dos {} valores é: {}'.format(i,soma))