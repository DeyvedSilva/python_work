salario = float(input('Qual é o slário do funcionário? R$'))
aumento = salario * 1.15
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, aumento))

# desafio extra
preco = float(input('Qual o preço do produto? R$'))
vista = preco - (preco * 10 / 100)
prazo = preco + (preco * 8 / 100)
print('O preço do produto é R${:.2f}. A vista ele sai por R${:.2f} e a prazo ficará por R${:.2f}.'.format(preco, vista, prazo))
