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

"""
# 7.4
prompt = '\nInforme o ingrediente da pizza.'
prompt += '\n(Para sair digite "quit"): '
while True:
    ingrediente = input(prompt)
    if ingrediente == 'quit':
        break
    print(f'Vamos acrescentar o ingrediente {ingrediente} à pizza.')

# 7.5
idade = '\nInforme sua idade.'
idade += '\n"quit" para sair: '
while True:
    if idade == 'quit':
        break
    if int(idade) < 3:
        print('O ingresso será gratuito!')
    elif int(idade) < 12:
        print('O ingresso custará 10 dólares.')
    else:
        print('O ingresso custará 15 dólares.')

# 7.6
