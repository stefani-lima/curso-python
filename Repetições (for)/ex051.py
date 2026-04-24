# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

a = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
decimo = a + (10 - 1) * r
for n in range(a, decimo + r, r):
    print(n)