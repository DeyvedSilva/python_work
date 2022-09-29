# exercícios do capítulo 7
"""
# 7.1
tipo_carro = input('Qual tipo de carro você gostaria de alugar? ')
print(f'Deixe-me ver se consigo um {tipo_carro} para você.')

# 7.2
qtd_pessoas = input('Quantas pessoas estão em seu grupo para jantar? ')
if int(qtd_pessoas) > 8:
    print('Vocês devem esperar uma mesa.')

# 7.3
num = input('informe um número: ')
if int(num) % 10 == 0:
    print(f'O número {num} é multiplo de dez.')
else:
    print(f'O número {num} não é multiplo de dez.')

# 7.4
prompt = '\nInforme o ingrediente da pizza.'
prompt += '\n(Para sair digite "quit"): '
while prompt != 'quit':
    ingrediente = input(prompt)
    print(f'Vamos acrescentar o ingrediente {ingrediente} à pizza.')

# 7.5
messsage = '\nInforme sua messsage.'
messsage += '\n"quit" para sair: '
while messsage != 'quit':
    idade = int(messsage)
    if idade < 3:
        print('O ingresso será gratuito!')
    elif idade < 12:
        print('O ingresso custará 10 dólares.')
    else:
        print('O ingresso custará 15 dólares.')

# 7.6
prompt = '\nInforme o ingrediente da pizza: '
active = 0
while active <= 8:
    ingrediente = input(prompt)
    print(f'Vamos acrescentar o ingrediente {ingrediente} à pizza')
    active += 1

# 7.7
while True:
    print('Isso é um laço infinito')
"""
# 7.8
sandwich_orders = ['x-tudo', 'x-bacon', 'x-salada', 'x-especial']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Preparei seu {sandwich}')
    finished_sandwiches.append(sandwich)
print('todos os pedidos prontos: ')
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

# 7.9
#  TODO
