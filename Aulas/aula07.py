# aula 07
print('oi' * 5)
print('oi' + 'olá')
print('=' * 20)

nome = input('Qual é seu nome')
print('Prazer em te conhecer {:20}!'.format(nome))
print('{:>20}'.format('teste'))
print('{:<20}'.format('caramba'))
print('{:^20}'.format('centralizado'))
print('{:+=^20}'.format('com firula'))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma é {0}, o produto é {1}, a subtração é {2};'.format(n1 + n2, n1 * n2, n1 - n2))
print('A divisão é {0}, a exponenciação é {1}, a divisão inteira é {2} e o resto da divisão é {3}.'.format(n1 / n2, n1 ** n2, n1 // n2, n1 % n2))
