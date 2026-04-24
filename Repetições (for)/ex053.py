# Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
texto_sem_espaco = frase.replace(" ", "" )
frase_espelhada = texto_sem_espaco[::-1]

if texto_sem_espaco == frase_espelhada:
    print('A frase é palíndromo!')
else:
    print('A frase não é palíndromo!')
print('Frase espelhada: {}'.format(frase_espelhada))
print('Frase original sem espaços: {}'.format(texto_sem_espaco))