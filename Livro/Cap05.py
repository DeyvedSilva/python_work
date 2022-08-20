# exercícios do capítulo 5
"""
# 5.1
var1 = True
var2: bool = False

print('var1 != var2? I predict True')
print(var1 != var2)

print('not var2 == var1? I predict True')
print(not var2 == var1)

print('var1 == var2 or var1 != var2? I predict True')
print(var1 == var2 or var1 != var2)

print('var1 == var2? I predict False')
print(var1 == var2)

print('not var1 != var2? I predict False')
print(not var1 != var2)

print('var1 == var2 and var1 != var2? I predict False')
print(var1 == var2 and var1 != var2)

# 5.2
a = 'asd'
b = 'asdf'
print(a == b)
print(a != b)
c = 'Asd'
print(c.lower() != a)
print(c.lower() == a)
print(1 == 2)
print(1 != 2)
print(2 >= 4)
print(3 <= 3)
print(3 > 3)
print(1 == 2 and 1 != 2)
print(1 == 2 or 1 != 2)
print(3 <= 3 and 3 <= 3)
print(c.lower() != a or c.lower() == a)
print('a' in a)
print('b' in b)
print(a in c)

# 5.3
alien_color = 'green'
if alien_color == 'green':
    print('Você ganhou 5 pontos!')
if alien_color == 'red':
    pass

# 5.4
alien_color = 'red'
if alien_color == 'green':
    print('Você ganhou 5 pontos!')
else:
    print('Você perdeu 5 pontos!')

alien_color = 'yellow'
if alien_color == 'yellow':
    print('Você ganhou 3 pontos!')
else:
    print('Game Over')

# 5.5
if alien_color == 'green':
    print('Você ganhou 5 pontos!')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos!')
else:
    print('Você ganhou 15 pontos!')

# 5.6
age = 35
if age < 2:
    print('Você é um bebê')
elif age < 4:
    print('Você é uma criança')
elif age < 13:
    print('Você é um garoto')
elif age < 20:
    print('Você é um adolescente')
elif age < 65:
    print('Você é um adulto')
else:
    print('Você é um idoso')

# 5.7
frutas_favoritas = ['maçã', 'uva', 'goiaba', 'manga', 'acerola', ]
if 'uva' in frutas_favoritas:
    print('Você realmente gosta de uvas!')
if 'banana' in frutas_favoritas:
    print('Você realmente gosta de bananas!')
if 'Goiaba' in frutas_favoritas:
    print('Você realmente gosta de Goiabas!')

"""
# 5.8
users = ['admin', 'Deyved', 'Davi', 'Jane', 'Giulia']
for user in users:
    if user == 'admin':
        print('Olá admin, gostaria de ver um relatório de status?')
    else:
        print(f'Olá {user}, obrigado por fazer login novamente.')

# 5.9
users.clear()
if not users:
    print('Precisamos encontrar alguns usuários!')

# 5.10
current_users = ['admin', 'Deyved', 'Davi', 'Jane', 'Giulia']
new_users = ['Laysa', 'Daniel', 'Pedro', 'Flávio', 'JANE']
for new_user in new_users:
    if new_user.title() in current_users:
        print(f'{new_user}, você deve fornecer um novo nome.')
    else:
        print(f'O nome {new_user} está disponível.')

# 5.11
ordinais = list(range(1, 10))
for ordinal in ordinais:
    if ordinal == 1:
        print(f'{ordinal}st', end=' ')
    elif ordinal == 2:
        print(f'{ordinal}nd', end=' ')
    elif ordinal == 3:
        print(f'{ordinal}rd', end=' ')
    else:
        print(f'{ordinal}th', end=' ')
print()

# 5.12
# já sigo o padrão da PEP 8 sobre testes condicionais

# 5.13
"""
jogos: aviões
"""
