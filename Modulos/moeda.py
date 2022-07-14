def aumentar(valor, taxa):
    novo = valor + (valor * taxa / 100)
    return novo


def diminuir(valor, taxa):
    novo = valor - (valor * taxa / 100)
    return novo


def dobro(valor):
    novo = valor * 2
    return novo


def metade(valor):
    novo = valor / 2
    return novo


def moeda(valor):
    formato = f'R${valor:.0f},00'
    return formato
