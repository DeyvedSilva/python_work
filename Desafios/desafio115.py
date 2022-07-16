from Modulos.validacao import *
from Modulos.lib import *

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

opcao = validar_opcao('\033[33mSua opção:\033[m ')
while True:
    if opcao == 1:
        menu_ver_cadastro()
        ler_arquivo(arq)
        opcao = validar_opcao('\033[33mSua opção:\033[m ')
    elif opcao == 2:
        menu_cadastrar()
        nome = str(input('Nome: '))
        idade = validar_inteiro('Idade: ')
        if idade != -1:
            salvar_arquivo(arq, nome, idade)
        opcao = validar_opcao('\033[33mSua opção:\033[m ')
    elif opcao == 3:
        menu_sair()
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        continue
