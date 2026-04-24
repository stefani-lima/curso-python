# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# -> A média de idade do grupo
# -> Qual é o homem mais velho
# -> Quantas mulheres têm menos de 20 anos

mais_velho = 0
nome_mais_velho = ''
menos_vinte = 0
soma_idade = 0

for i in range(1, 5):
    print('Pessoa {}'.format(i))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome

    elif sexo == 'F':
        if idade < 20:
            menos_vinte += 1
    else:
        print('Por favor, digite apenas M ou F.')

media_idade = soma_idade / 4

print('A média de idade do grupo é: {}'.format(media_idade))
print('O homem mais velho é {} e tem {} anos'.format(nome_mais_velho, mais_velho))
print('{} mulheres têm menos de 20 anos'.format(menos_vinte))