# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# -> À vista dinheiro/cheque: 10% de desconto
# -> À vista no cartão: 5% de desconto
# -> Em até 2x no cartão: preço normal
# -> 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto: '))
condicao = input('''Qual será a forma de pagamento? 
[1] - Dinheiro
[2] - Cheque
[3] - À vista no cartão
[4] - Em até 2x no cartão
[5] - 3x ou mais no cartão
''')
if condicao == 1 or 2:
    valor_final = valor_produto - (valor_produto * 0.1)
    print('Valor total: {}'.format(valor_final))
elif condicao == 3:
    valor_final = valor_produto - (valor_produto * 0.05)
    print('Valor total: {}'.format(valor_final))
elif condicao == 4:
    valor_final = valor_produto
    print('Valor total: {}'.format(valor_final))
elif condicao == 5:
    valor_final = valor_produto * 1.20
    print('Valor total: {}'.format(valor_final))
else:
    print('Forma de pagamento não identificada, por favor tente novamente.')
