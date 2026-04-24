''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
-> Quantas pessoas tem mais de 18 anos.
-> Quantos homens foram cadastrados.
-> Quantas mulheres tem menos de 20 anos.'''

cont = 1
maior = 0
homens = 0
mulheres = 0

while True:
    print('-' * 30)
    print(f'CADASTRO DA {cont}° PESSOA')

    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    cont += 1

    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1

    confirmacao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while confirmacao not in 'SN':
        confirmacao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if confirmacao == 'N':
        break

print('-+' * 30)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')
