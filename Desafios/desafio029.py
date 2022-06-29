velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    diferenca = velocidade - 80
    total = 7 * diferenca
    print('Você foi multado. E a multa é no valor de R${:.2f}'.format(total))
else:
    print('Tenha um bom dia! Dirija com segurança!')
