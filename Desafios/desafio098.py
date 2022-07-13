def contador(i, f, p):
    print('-=' * 30)
    if p == 0:
        p = 1
    if p < 0:
        p = abs(p)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        while i >= f:
            print(f'{i}', end=' ')
            i -= p
        print('FIM!')
    elif i < f:
        while i <= f:
            print(f'{i}', end=' ')
            i += p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
