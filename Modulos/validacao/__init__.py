from Modulos.interface import *


def validar_opcao(msg):
    while True:
        try:
            criar_menu()
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário desistiu')
            break
        else:
            if num == 1:
                return 1
            elif num == 2:
                return 2
            elif num == 3:
                return 3
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
                continue


def validar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número para idade válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário desistiu')
            return -1
        else:
            if num < 0:
                num = abs(num)
                return num
            else:
                return num
