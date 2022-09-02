# exercícios do capítulo 6
""""""
# 6.1
pessoa_0 = {'first name': 'Deyved', 'last name': 'Silva', 'age': 36, 'city': 'Cariacica'}
for chave, valor in pessoa_0.items():
    print(f'{chave}: {valor}')

# 6.2
numeros_favoritos = {'Jane': 46, 'Deyved': 36, 'Giulia': 18, 'Pedro': 6, 'Davi': 4, }
for nome, valor in numeros_favoritos.items():
    print(f'{nome}:\t {valor}')

# 6.3
glossario = {'and': 'operador lógico', 'or': 'operador lógico', 'not': 'operador lógico', 'print': 'função',
             'modulos': 'funções de classes', }
for chave, valor in glossario.items():
    print(f'{chave}: \n\t{valor}')

# 6.4
glossario['in'] = 'Está na lista'
glossario['class'] = 'Classe, molde para criar objetos'
glossario['if'] = 'instrução condicional'
glossario['for'] = 'laço de repetição'
glossario['while'] = 'laço de repetição'
for chave, valor in glossario.items():
    print(f'{chave}: {valor}')

# 6.5
rios = {'nilo': 'egito', 'amazonas': 'brasil', 'ganges': 'índia'}
for chave, valor in rios.items():
    print(f'O {chave.title()} corre pelo(a) {valor.title()}.')
for name in rios:
    print(name.title())
for pais in rios.values():
    print(pais.title())

# 6.6
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
pessoas = ['edward', 'maria', 'josé', 'phil']
for pessoa in sorted(pessoas):
    if pessoa in favorite_languages:
        print(f'{pessoa}, obrigado por participar da enquete.')
    else:
        print(f'{pessoa}, vamos participar da enquete!')

# 6.7
pessoa_1 = {'first name': 'Jane', 'last name': 'Silva', 'age': 46, 'city': 'Cariacica'}
pessoa_2 = {'first name': 'Davi', 'last name': 'Silva', 'age': 4, 'city': 'Cariacica'}
people = [pessoa_0, pessoa_1, pessoa_2]
for gente in people:
    print(gente)

# 6.8
pet_0 = {'tipo': 'cão', 'dono': 'João', }
pet_1 = {'tipo': 'gato', 'dono': 'João', }
pet_2 = {'tipo': 'cão', 'dono': 'Eduardo', }
pet_3 = {'tipo': 'gato', 'dono': 'Maria', }
pets = [pet_0, pet_1, pet_2, pet_3]
for pet in pets:
    print(pet)

# 6.9
favorite_places = {'Deyved': ['PE', 'CE'], 'Jane': ['RJ', 'BA', 'ES'], 'Giulia': ['RJ'], }
for pessoa, lugar in favorite_places.items():
    print(f'nome: {pessoa}, lugares favoritos: {lugar}')

# 6.10
numeros_favoritos = {'Jane': [46], 'Deyved': [36, 16, 64], 'Giulia': [18], 'Pedro': [6, 10], 'Davi': [4, 5, 2], }
for nome, valor in numeros_favoritos.items():
    print(f'{nome}:\t {valor}')

# 6.11
cities = {'Rio de Janeiro': {'country': 'Brasil', 'population': 150000, 'fact': 'sudeste'},
          'Recife': {'country': 'Brasil', 'population': 145000, 'fact': 'nordeste'},
          'Vitória': {'country': 'Brasil', 'population': 120000, 'fact': 'sudeste'}, }
for city, city_inf in cities.items():
    print(f'\nCidade: {city}')
    pais = city_inf['country']
    populacao = city_inf['population']
    fato = city_inf['fact']
    print(f'País: \t{pais}')
    print(f'População: \t{populacao}')
    print(f'Fato: \t{fato}')
