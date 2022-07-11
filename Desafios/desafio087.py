lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-=' * 30)
maior = pares = terc = 0
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]', end='')
        if lista[i][j] % 2 == 0:
            pares += lista[i][j]
        if j == 2:
            terc += lista[i][j]
        if i == 1 and lista[i][j] > maior:
            maior = lista[i][j]
    print()
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terc}.')
print(f'O maior valor valor da segunda linha é {maior}')
