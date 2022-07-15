from Modulos import *


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO! O arquivo não foi criado.')
    else:
        print(f'Aruivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'ERRO! Não foi possível ler o arquivo {nome}')
    else:
        menu_ver_cadastro()
        print(a.read())


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True
