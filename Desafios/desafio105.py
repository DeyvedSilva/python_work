def notas(*nota, situ=False):
    """
    -> Função que calcula a média
    :param nota: lista de notas
    :param situ: situação das notas (boa, ruim, regular e excelente)
    :return: um dicionário com as informações
    """
    dici = {'total': len(nota), 'maior': max(nota), 'menor': min(nota), 'media': sum(nota) / len(nota)}
    if situ:
        if dici['media'] < 5:
            dici['situacao'] = 'RUIM'
        elif dici['media'] < 7:
            dici['situacao'] = 'REGULAR'
        elif dici['media'] < 9:
            dici['situacao'] = 'BOA'
        else:
            dici['situacao'] = 'EXCELENTE'
    return dici


resp = notas(5.5, 9.5, 10, 6.5, situ=True)
print(resp)
