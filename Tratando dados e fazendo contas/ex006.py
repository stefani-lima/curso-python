# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número para saber o seu dobro, triplo e raiz quadrada: '))
print('O número escolhido {}, tem como o seu dobro {}, o triplo {} e a raiz quadrada {:.3f}!'.format(num,num*2,num*3,num**(1/2)))