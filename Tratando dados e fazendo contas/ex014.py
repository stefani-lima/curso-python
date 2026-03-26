# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Qual a temperatura em graus celsius? '))
fahrenheit = (celsius * 1.8) + 32
print('A temperatura de {:.0f}°C, convertida para Fahrenheit, é {}°F.'.format(celsius, fahrenheit))