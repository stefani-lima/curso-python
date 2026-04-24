''' Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
-> Qual é o total gasto na compra.
-> Quantos produtos custam mais de R$ 1.000,00.
-> Qual é o nome do produto mais barato.'''

total = cont = barato = totmil = 0
nome_barato = ''

while True:
    produto = str(input('Qual é o nome do produto: ')).strip()
    preco = float(input('Qual é o preço do produto: R$ '))
    print('-' * 30)
    cont += 1
    total += preco

    if cont == 1 or preco < barato:
        barato = preco
        nome_barato = produto
    if preco > 1000:
        totmil += 1

    confirmacao = ' '
    while confirmacao not in 'SN':
        confirmacao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if confirmacao == 'N':
        break

print('-'*30)
print(f'O total gasto na compra foi de: R$ {total}')
print(f'{totmil} produtos custam mais de R$ 1.000,00.')
print(f'O nome do produto mais barato é: {nome_barato}')