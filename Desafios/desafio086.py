lista = [[], [], []]
a = b = 0
for i in range(0, 9):
    num = int(input(f'Digite um valor para [{a}, {b}]: '))
    b += 1
    lista[a].append(num)
    if b == 3:
        a += 1
        b = 0
print('~-' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^3}]', end='')
    print()

