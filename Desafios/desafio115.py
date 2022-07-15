from Modulos.validacao import *
from Modulos.lib import *

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

validar_opcao('\033[33mSua opção:\033[m ', arq)
