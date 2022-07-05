num = int(input('Informe um número: '))
ant1, ant2 = 0, 1
while num != 0:
    print('{}'.format(ant1), end=' -> ')
    temp = ant2 + ant1
    ant1 = ant2
    ant2 = temp
    num -= 1
print('Fim')
