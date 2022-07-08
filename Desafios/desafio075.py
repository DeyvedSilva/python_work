num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))
num5 = int(input('Digite um número: '))
tupla = (num1, num2, num3, num4, num5)
cont = 0
for c in tupla:
    if c == 9:
        cont += 1
print(f'O número 9 apareceu {cont} vezes')
print(f'O número 3 está na posição {tupla.index(3) + 1}')
print('Os pares são ', end='')
for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i], end=' ')
