def aumentar(valor, taxa, formatacao=False):
    novo = valor + (valor * taxa / 100)
    if formatacao:
        return moeda(novo)
    else:
        return novo


def diminuir(valor, taxa, formatacao=False):
    novo = valor - (valor * taxa / 100)
    return novo if not formatacao else moeda(novo)


def dobro(valor, formatacao=False):
    novo = valor * 2
    return novo if not formatacao else moeda(novo)


def metade(valor, formatacao=False):
    novo = valor / 2
    if formatacao:
        return moeda(novo)
    else:
        return novo


def moeda(valor):
    formato = f'R${valor:.2f}'.replace('.', ',')
    return formato
