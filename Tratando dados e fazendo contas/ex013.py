# Faça um que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

salario = float(input('Informe o valor do seu salário: R$ '))
print('O novo salário com um aumento de 15% é: R$ {:.2f}! '.format(salario * 1.15))