# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados (unidade, dezena, centena e milhar)

num = int(input('Digite um número de 0 a 9999: '))
n = str(num)

print('Unidade:',n[3])
print('Dezena:',n[2])
print('Centena:',n[1])
print('Milhar:',n[0])

