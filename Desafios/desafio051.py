termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
for c in range(termo, termo + 10 * razao, razao):
    print(c, end=' -> ')
print('Acabou')
