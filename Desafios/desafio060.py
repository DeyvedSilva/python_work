num = inicio = int(input('Digite um número: '))
fat = 0
while inicio != 0:
    if inicio == num:
        fat = inicio
    else:
        fat *= inicio
    inicio -= 1
print('O fatorial de {}! é {}'.format(num, fat))
