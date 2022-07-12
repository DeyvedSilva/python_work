from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
rank = dict()
print('Valores sorteados:')
for i in range(1, 5):
    jogo = {'Nome': f'jogador{i}', 'Valor': randint(1, 6)}
    sleep(1)
    print(f'O {jogo["Nome"]} tirou {jogo["Valor"]}')
print('-' * 30)
print('Ranking dos jogadores:')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
