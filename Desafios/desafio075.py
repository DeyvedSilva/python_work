tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 está na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não aparece em nenhuma posição')
print('Os pares são ', end='')
for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i], end=' ')
