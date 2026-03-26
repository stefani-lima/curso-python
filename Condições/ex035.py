# Desenvolva um programa que leia o comprimento de três retas e digam ao usuário se elas podem ou não formar um triângulo.

print('Digite o comprimento de A, B e C, respectivamente.')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')