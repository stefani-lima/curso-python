# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule o comprimento da hipotenusa

from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
