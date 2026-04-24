''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
 Considere que o caixa terá notas de R$50, R$20, R$10 e R$1'''

cinquenta = vinte = dez = um = 0
print('-'*30)
saque = int(input('Digite o valor da saque: '))
print('-'*30)
total = saque

while total != 0:
    if total >= 50:
        total -= 50
        saque = total
        cinquenta += 1
    elif total >= 20:
        total -= 20
        saque = total
        vinte += 1
    elif total >= 10:
        total -= 10
        saque = total
        dez += 1
    elif total >= 1:
        total -= 1
        saque = total
        um += 1

print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('-+'*15)
print('FIM DO PROGRAMA')