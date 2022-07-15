import Modulos
from time import sleep


def validar_opcao(msg):
    while True:
        try:
            Modulos.criar_menu()
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.')

        except KeyboardInterrupt:
            print('O usuário desistiu')
            break
        else:
            if num == 1:
                Modulos.menu_ver_cadastro()
            elif num == 2:
                Modulos.menu_cadastrar()
            elif num == 3:
                Modulos.menu_sair()
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
                continue
