num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num2 > num1:
    print('O segundo valor é maior.')
elif num1 > num2:
    print('O primeiro valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
