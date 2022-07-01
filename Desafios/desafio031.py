distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('O preço da sua passagem é {:.2f}.'.format(preco))
