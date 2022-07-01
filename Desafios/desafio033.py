num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    maior = num1
    if num2 < num3:
        menor = num2
    else:
        menor = num3
elif num2 > num3:
    maior = num2
    if num1 < num3:
        menor = num1
    else:
        menor = num3
else:
    maior = num3
    if num1 < num2:
        menor = num1
    else:
        menor = num2
print('O número {} é o maior.'.format(maior))
print('O número {} é o menor.'.format(menor))
