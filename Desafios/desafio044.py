preco = float(input('Informe o preço do produto: R$'))
print("""Qual a forma de pagamento: 
1 - à vista (dinheiro/cheque com 10% de desconto)
2 - à vista (cartão com 5% de desconto)
3 - até 2x no cartão (sem juros)
4 - em 3x ou mais no cartão (juros de 20%)""")
opcao = input('A opção desejada é: ')
print('O valor atual do produto é R${:.2f}'.format(preco))
print('De acordo com a opção {} escolhida o novo valor é R$'.format(opcao), end='')
if opcao == '1':
    print('{}.'.format(preco * 0.9))
elif opcao == '2':
    print('{}.'.format(preco * 0.95))
elif opcao == '3':
    print('{}.'.format(preco))
else:
    print('{}.'.format(preco * 1.2))
