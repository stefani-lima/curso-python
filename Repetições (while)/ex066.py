''' Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag). '''

cont = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print('FIM')
print('A soma dos valores foi: {}'.format(soma))
print('Foram digitados {} números'.format(cont))