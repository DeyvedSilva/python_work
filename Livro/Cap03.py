# exercícios do capítulo 3
# 3.1
names = ['Jane', 'Davi', 'Giulia', 'Deyved', 'Douglas', 'Flavio', 'Deyvson']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

# 3.2
print(f'Olá, {names[0]} como você está?')
print(f'Olá, {names[1]} como você está?')
print(f'Olá, {names[2]} como você está?')
for i in names:
    print(f'Olá, {i} como você está?')

# 3.3
transporte = ['honda', 'toyota', 'bmw']
print(f'Gostaria de ter um carro {transporte[0].upper()}.')
print(f'Gostaria de ter um carro {transporte[1].upper()}.')
print(f'Gostaria de ter um carro {transporte[2].upper()}.')

# 3.4
lista_convidados = ['Elvis', 'Senna', 'Xuxa']
print(f'{lista_convidados[0]}, Gostaria de convidar você para meu jantar.')
print(f'{lista_convidados[1]}, gostaria de convidar você para meu jantar.')
print(f'{lista_convidados[2]}, gostaria de convidar você para meu jantar.')

# 3.5
print(f'{lista_convidados[2]} não poderá comparecer!')
lista_convidados[2] = 'Ronaldo'
print(f'{lista_convidados[0]} está cofirmado.')
print(f'{lista_convidados[1]} está confirmado.')
print(f'{lista_convidados[2]} está confirmado.')

# 3.6
print(f'{lista_convidados}, encontrei uma mesa maior.')
lista_convidados.insert(0, 'Jane')
lista_convidados.insert(2, 'Davi')
lista_convidados.append('Giulia')
for convite in lista_convidados:
    print(f'{convite.capitalize()}, gostaria de convidar você para meu jantar.')

# 3.7
print('Infelizmente, só vou poder convidar duas pessoas.')
sair = lista_convidados.pop(0)
print(f'{sair}, infelizmente não posso convidar você para o jantar.')
sair = lista_convidados.pop(1)
print(f'{sair}, infelizmente não posso convidar você.')
sair = lista_convidados.pop(2)
print(f'{sair}, infelizmente não posso convidar você para o jantar.')
sair = lista_convidados.pop()
print(f'{sair}, infelizmente não posso convidar você para o jantar.')
print(f'{lista_convidados[0]}, aguardo você no meu jantar.')
print(f'{lista_convidados[1]}, aguardo você no meu jantar.')
# del lista_convidados
print(lista_convidados)

# 3.8
lugares = ['Toronto', 'Disney', 'Porto', 'New York', 'Lisboa']
print(lugares)
print(sorted(lugares))
print(lugares)
print(sorted(lugares, reverse=True))
print(lugares)
lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)

# 3.9
print(f'Temos {len(lista_convidados)} convidados para o jantar.')

# 3.11
motorcycles = []
# Tipo de erro: IndexError
# print(motorcycles[-1])
# print(lugares[5])
