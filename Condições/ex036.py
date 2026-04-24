# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa? R$ '))
salario_comprador = float(input('Qual é o seu salário atual? '))
anos = int(input('Em quantos anos você irá pagar a casa? '))
valor_mensal = valor_casa / (anos * 12)

if valor_mensal > (salario_comprador * 0.30):
    print('O seu empréstimo foi negado!')
else:
    print('O seu empréstimo foi aprovado! Parabéns!')