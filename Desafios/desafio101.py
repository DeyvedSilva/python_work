def voto(a):
    from datetime import date
    ano_atual = date.today().year
    i = ano_atual - a
    if 18 < i < 65:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    elif i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    else:
        return f'Com {i} anos: VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
