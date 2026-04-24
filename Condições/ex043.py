# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status de acordo com:
# -> Abaixo de 18,50: ABAIXO DO PESO
# -> Entre 18,50 e 25: PESO IDEAL
# -> 25 até 30: SOBREPESO
# -> 30 até 40: OBESIDADE
# -> Acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O aluno está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('O aluno está com peso ideal!')
elif imc >= 25 and imc < 30:
    print('O aluno está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('O aluno está com obesidade!')
else:
    print('O aluno está com obesidade mórbida!')