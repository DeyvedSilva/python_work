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


def resumo(preco, taxaa, taxar):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
