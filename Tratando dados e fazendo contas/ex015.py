'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km_percorridos = float(input('Quantos kilometros foram percorridos? '))
dias_alugados = int(input('Quantos dias alugados? '))
preco = (dias_alugados * 60) + (km_percorridos * 0.15)
print('O valor total a pagar é R$ {:.2f}'.format(preco))