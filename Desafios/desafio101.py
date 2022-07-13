from datetime import datetime

ano_atual = datetime.today().year


def voto(a):
    i = ano_atual - a
    if 18 < i < 65:
        return 'VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return 'NÃO VOTA.'
    else:
        return 'VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano
print(f'Com {idade} anos: {voto(ano)}')
