def contador(i, f, p):
    """
    -> faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    pass


def somar(a, b, c=0):
    # variável local
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(b=7, a=9)

# variável global
d = 5


def subtrair(a=0, b=0):
    s = a - b
    return s


resp = subtrair(10, 2)
r1 = subtrair()
print(f'Os resultados foram {resp} e {r1}.')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(fatorial(n))
