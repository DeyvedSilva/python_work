produtos = ('Mouse', 50, 'Teclado', 100, 'Monitor', 400, 'Fonte', 200, 'Som', 450)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}R${produtos[c + 1]:>7.2f}')
