valor = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 3.27
print('Com R${} você pode comprar US${:.2f}.'.format(valor, valor/dolar))
