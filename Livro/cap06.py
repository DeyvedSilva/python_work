# exercícios do capítulo 6
""""""
# 6.1
pessoa = {'first name': 'Deyved', 'last name': 'Silva', 'age': 36, 'city': 'Cariacica'}
for chave, valor in pessoa.items():
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
