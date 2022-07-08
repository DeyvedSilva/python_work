tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso')
for c in range(0, len(tupla)):
    item = tupla[c]
    print(f'Na palavra {item} temos ', end='')
    for i in item:
        if i in 'aeiou':
            print(i, end=' ')
    print()
