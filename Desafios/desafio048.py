s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print('A soma dos ímpares multiplos de 3 é {}'.format(s))