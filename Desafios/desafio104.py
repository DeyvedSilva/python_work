def leiaint(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[31mERRO! Digite um númeo inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
