# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# -> Até 9 anos: MIRIM
# -> Até 14 anos: INFANTIL
# -> Até 19 anos: JUNIOR
# -> Até 20 anos: SÊNIOR
# -> Acima: MASTER

from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('Você está na categoria MIRIM!')
elif (idade > 9) and (idade <= 14):
    print('Você está na categoria INFANTIL!')
elif (idade > 14) and (idade <= 19):
    print('Você está na categoria JUNIOR!')
elif idade == 20:
    print('Você está na categoria SÊNIOR!')
else:
    print('Você está na categoria MASTER!')