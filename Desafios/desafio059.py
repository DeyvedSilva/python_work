num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
    opcao = int(input('Qual opção desejada: '))
    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num2 > num1:
            print('O número {} é maior.'.format(num2))
        else:
            print('O número maior é {}.'.format(num1))
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Obrigado!')
