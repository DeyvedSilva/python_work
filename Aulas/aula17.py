num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei!')
print(num)


valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encotrei o valor {v}')
print('Cheguei ao final da lista.')


a = [2, 3, 4, 7]
b = a
print(a, b)
b[2] = 8
print(a, b)
c = a[:]
print(a, b, c)
c[1] = 9
print(a, b, c)
