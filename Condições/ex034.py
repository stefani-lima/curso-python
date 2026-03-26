''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
 Para salários inferiores ou iguais, calcular um aumento de 15%. '''

salario = float(input('Qual é o seu salário atual? '))
if salario > 1250:
    print('O seu salário atual de R$ {}, com um aumento de 10%, passa a ganhar: R$ {}.'.format(salario, salario * 1.10))
else:
    print('O seu salário atual de R$ {}, com um aumento de 15%, passa a ganhar: R$ {}.'.format(salario, salario * 1.15))
