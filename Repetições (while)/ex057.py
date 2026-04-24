'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter o valor correto.'''

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf' :
    sexo = str(input('Opção de resposta inválida, digite novamente: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
