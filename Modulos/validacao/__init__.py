from Modulos.interface import *
from Modulos.lib import *


def validar_opcao(msg, arq):
    while True:
        try:
            criar_menu()
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O usuário desistiu')
            break
        else:
            if num == 1:
                menu_ver_cadastro()
                ler_arquivo(arq)
                continue
            elif num == 2:
                menu_cadastrar()
            elif num == 3:
                menu_sair()
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
                continue
