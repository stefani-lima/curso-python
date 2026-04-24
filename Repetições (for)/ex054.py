# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maior = 0
menor = 0
for i in range(1, 7+1):
    ano_nascimento = int(input('Ano de nascimento (Pessoa {}): '.format(i)))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas maiores de idade'.format(maior))
print('{} pessoas menores de idade'.format(menor))
