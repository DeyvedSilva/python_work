def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um númeo
    :param n: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número
    """
    f = 1
    c = n
    if not show:
        for i in range(n, 0, -1):
            f *= i
        return f
    else:
        for j in range(n, 0, -1):
            f *= j
            if j > 1:
                print(f'{c}', end=' x ')
                c -= 1
            else:
                return f'{c} = {f}'


print('-' * 30)
print(fatorial(5, True))

