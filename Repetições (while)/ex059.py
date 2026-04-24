'''Crie um programa que leia dois valores e mostre um menu na tela:
- [1] Somar
- [2] Multiplicar
- [3] Maior
- [4] Novos números
- [5] Sair do programa
Seu programa deverá realizar as operações solicitadas em cada caso.'''
menu = 0
soma = 0
multiplicacao = 0

while menu != 6:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    menu = int(input("""
    - [1] Somar
    - [2] Multiplicar
    - [3] Maior
    - [4] Novos números
    - [5] Sair do programa
    Digite uma das opções acima:  """))

    if menu == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é: {}'.format(num1, num2, soma))
    elif menu == 2:
        multiplicacao = num1 * num2
        print('A multiplicação entre {} e {} é: {}'.format(num1, num2, multiplicacao))
    elif menu == 3:
        if num1 > num2:
            print('O primeiro valor é maior!')
        elif num2 > num1:
            print('O segundo valor é maior!')
        else:
            print('Os dois valores são iguais!')
    elif menu == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Saindo do programa...')
        break
    else:
        print('Você digitou uma opção inválida, tente novamente.')




