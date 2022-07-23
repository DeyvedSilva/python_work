# exercício do capítulo 3
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
