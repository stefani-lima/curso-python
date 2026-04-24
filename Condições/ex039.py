# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# -> Se ele ainda vai se alistar ao serviço militar
# -> Se é a hora de se alistar
# -> Se já passou do tempo de alistamento
# Seu programa também deverá mostrar quanto tempo falta ou que passou do prazo.

from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print('Falta {} ano(s) para você se alistar!'.format((18 - idade)))
elif idade == 18:
    print('Você está na hora de se alistar!')
else:
    print('Você já passou {} ano(s) do prazo de alistamento!'.format((idade - 18)))