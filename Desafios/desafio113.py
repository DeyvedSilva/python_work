def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um númeo inteiro válido\033[m.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            return 0
        else:
            return num


def leiafloat(txt):
    try:
        num = float(input(txt))
    except (ValueError, TypeError):
        print('\033[0;31mERRO! Digite um número real válido\033[m.')
    else:
        return num


n = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {n2}')
