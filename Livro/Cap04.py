# exercícios do capítulo 4
# 4.1
pizzas_favoritas = ['Franbacon', 'Frango com catupyri', 'Portuguesa']
for pizza in pizzas_favoritas:
    print(f'Gosto de pizza de {pizza}.')

print('Eu realmente adoro pizza!\n')

# 4.2
animais = ['belo', 'cooke', 'negão']
for animal in animais:
    print(f'O {animal.title()} é um ótimo animal de estimação.')
print('Qualquer um desses animais é um ótimo animal de estimação!\n')

# 4.3
for value in range(1, 21):
    print(value)

# 4.4
lista = list(range(1, 1000001))
# for item in lista:
#     print(item)

# 4.5
print(f'Mínimo é {min(lista)}')
print(f'Máximo é {max(lista)}')
print(f'Soma é {sum(lista)}')

# 4.6
for i in range(1, 21, 2):
    print(i)

# 4.7
tres = list(range(3, 31, 3))
for j in tres:
    print(j)

# 4.8
cubos = list(range(1, 11))
for i in cubos:
    print(i**3)

# 4.9
cubos_c = [valor**3 for valor in range(1, 11)]
for d in cubos_c:
    print(d)

# 4.10
print('Os três primeiros itens da lista são: ')
for item in cubos_c[0:3]:
    print(item)

print('Os três itens do meio da lista são: ')
meio = len(cubos_c) // 2
for item in cubos_c[(meio-1):(meio+2)]:
    print(item)

print('Os três últimos itens da lista são: ')
for item in cubos_c[-3:]:
    print(item)

# 4.11
friend_pizzas = pizzas_favoritas[:]
pizzas_favoritas.append('Brigadeiro')
friend_pizzas.append('Margerita')
print('Minhas pizzas favoritas são: ')
for i in pizzas_favoritas:
    print(i)
print('As pizzas favoritas de meu amigo são: ')
for j in friend_pizzas:
    print(j)

# 4.12
for item in pizzas_favoritas:
    print(item)
for food in pizzas_favoritas:
    print(food)

# 4.13
foods = 'feijoada', 'churrasco', 'lasanha', 'pudim', 'escondidinho'
# foods[1] = 'Tropeiro'
for food in foods:
    print(food)
foods = 'feijoada', 'churrasco', 'lasanha', 'pizza', 'Tropeiro'
for food in foods:
    print(food)
