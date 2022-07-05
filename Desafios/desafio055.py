maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa (Kg): '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O menor peso foi {}kg e o maior foi {}Kg.'.format(menor, maior))
