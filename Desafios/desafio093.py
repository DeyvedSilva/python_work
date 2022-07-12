gols = []
cont = 0
jogador = {'Nome': str(input('Nome do jogador: '))}
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i}? '))
    gols.append(gol)
    cont += gol
print('-=' * 30)
jogador['gols'] = gols[:]
jogador['total'] = cont
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(gols):
    print(f'   => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
