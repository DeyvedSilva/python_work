def funcao(func):
    tam = len(func) + 4 + len('Acessando o manual do comando ')

    print('\033[44m~' * tam)
    print(f'Acessando o manual do comando {func}'.center(tam))
    print('~' * tam)
    print(f'\033[7:40m{help(func)}')
    print()


funcao(str(input('Função ou Biblioteca > ')))
