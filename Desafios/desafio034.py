salario = float(input('Informe o valor do seu salário: '))
if salario > 1250:
    print('O seu aumento é de 10% e fica no valor de R${:.2f}'.format(salario * 1.1))
else:
    print('O seu aumento é de 15% e fica no valor de R${:.2f}'.format(salario * 1.15))
