from random import randint
numeros = []


def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
        print(num, end=' ')
    print('PRONTO!')


def soma_par():
    soma = 0
    for j in numeros:
        if j % 2 == 0:
            soma += j
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sortear()
soma_par()
