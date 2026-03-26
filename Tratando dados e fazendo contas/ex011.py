''' Faça um programa que leia a largura e a altura de uma parede em metros,
calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
pinta uma área de 2m2.'''

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
tinta = area / 2
print('A área total do local é de: {} metros quadrados, para essa área, serão necessários {} litros de tinta'.format(area, tinta))