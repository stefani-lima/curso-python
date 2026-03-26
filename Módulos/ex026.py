''' Faça um programa que leia uma frase pelo teclado e mostre:
 -> Quantas vezes aparecem a letra "A"
 -> Em que posição ela aparece a primeira vez
 -> Em que posição ela aparece pela última vez '''

frase = str(input('Digite uma frase: ')).strip().upper()
print('"A" aparece {} vezes'.format(frase.count('A')))
print('"A" aparece a primeira vez na posição {}'.format(frase.find('A')))
print('"A" aparece a última vez na posição {}'.format(frase.rfind('A')))
