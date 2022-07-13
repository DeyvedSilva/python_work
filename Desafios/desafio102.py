def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um númeo
    :param n: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print('-' * 30)
print(fatorial(5, True))

