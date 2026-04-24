# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem:
# -> Média abaixo de 5.0, REPROVADO
# -> Média entre 5.0 e 6.9, RECUPERAÇÃO
# -> Média acima de 7.0, APROVADO

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print('Você foi aprovado!')
elif media < 5:
    print('Você foi reprovado!')
else:
    print('Você está em recuperação!')