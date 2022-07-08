brasileirao = ('Palmeiras', 'Athletico Paranaense', 'Atlético Mineiro', 'Corinthians', 'Internacional',
               'Fluminense', 'São Paulo', 'Flamengo', 'Botafogo', 'Santos', 'Avaí', 'Coritiba', 'América Fc Saf',
               'Red Bull Bragantino', 'Ceará', 'Atlético', 'Goiás', 'Cuiabá Saf', 'Juventude', 'Fortaleza')
print(f'Os cinco primeiros são: {brasileirao[0:5]}')
print('~' * 30)
print(f'Os quatros últimos são: {brasileirao[-4:]}')
print('=' * 30)
print(f'Os times em orfem alfabética: {sorted(brasileirao)}')
print('-' * 30)
print(f'Em qual posição está o time da Ceaá: {brasileirao.index("Ceará") + 1}ª posição')
