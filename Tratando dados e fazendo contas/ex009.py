# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = (int(input('Digite um valor para exibir a sua tabuada: ')))
for i in range(11):
    print('{} X {} = {}'.format(num, i, num * i))
