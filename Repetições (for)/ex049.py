# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que utilizando for.

num = (int(input('Digite um valor para exibir a sua tabuada: ')))
for i in range(11):
    print('{} X {} = {}'.format(num, i, num * i))