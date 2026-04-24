# Refaça o desafio 35 dos triângulos, acrescentando que tipo de triângulo será formado:
# -> Equilátero: todos os lados iguais
# -> Isósceles: dois lados iguais
# -> Escaleno: todos os lados diferentes

print('Digite o comprimento de A, B e C, respectivamente.')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c and c == a:
        print('O triângulo é do tipo EQUILÁTERO!')
    elif (a == b) and (a != c) or (b == c) and (c != a) or (a == c) and (b != c):
        print('O triângulo é do tipo ISÓSCELES!')
    else:
        print('O triângulo é do tipo ESCALENO!')
else:
    print('Não é possível formar um triângulo!')