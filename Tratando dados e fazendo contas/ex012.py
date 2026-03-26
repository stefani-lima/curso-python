# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o valor do produto? R$ '))
print('O novo valor do produto com um desconto de 5% é: R$ {}! '.format(preco - (preco * 0.05)))