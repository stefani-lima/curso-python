# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Escreva um valor em metros: '))
centimetros = metros * 100
milimetros = centimetros * 1000
print('{} metros se convertido, é igual a {:.0f}cm  e {:.0f}mm.'.format(metros, centimetros, milimetros))