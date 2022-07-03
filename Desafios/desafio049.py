num = int(input('De qual número você quer ver a tabuada? '))
for c in range(1, 11):
    print('{:2} x {} = {:2}'.format(c, num, c * num))
