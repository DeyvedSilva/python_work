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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<50}\t{dado[1]:>3} anos')
    finally:
        a.close()


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def salvar_arquivo(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()
