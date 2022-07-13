from time import sleep
c = ('\033[m',          # 0 - sem cors
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def funcao(func):
    titulo(f'Acessando o manual do comando \'{func}\'', 4)
    print(c[6], end='')
    help(func)
    print(c[0], end='')
    sleep(2)


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        funcao(comando)
titulo('ATÉ LOGO', 1)
