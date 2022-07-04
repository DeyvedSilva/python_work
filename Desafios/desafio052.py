num = int(input('Informe um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('\nO número {} foi dividido {} vezes'.format(num, cont))
print('E por isso ele ', end='')
if cont == 2:
    print('é PRIMO')
else:
    print('NÂO é PRIMO')
