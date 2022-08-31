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
