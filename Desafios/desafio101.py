from datetime import datetime

ano_atual = datetime.today().year


def voto(a):
    global i
    i = ano_atual - a
    if 18 < i < 65:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    elif i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    else:
        return f'Com {i} anos: VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
