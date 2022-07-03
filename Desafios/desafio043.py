peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / altura ** 2
print('Seu IMC é \033[31m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
