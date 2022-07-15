from time import sleep


def linha():
    print('-' * 60)


def criar_menu():
    linha()
    print('MENU PRINCIPAL'.center(60))
    linha()
    sleep(0.5)
    print("""\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m
\033[33m3\033[m - \033[34mSair do sistema\033[m""")
    linha()


def menu_ver_cadastro():
    linha()
    print('Opção 1'.center(60))
    linha()
    sleep(1)
    return


def menu_cadastrar():
    linha()
    print('Opção 2'.center(60))
    linha()
    sleep(1)
    return


def menu_sair():
    linha()
    print('Saindo do sistema... Até logo!'.center(60))
    linha()
    sleep(1.5)
    return
