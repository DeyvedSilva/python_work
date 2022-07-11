from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

lista = []
jogo = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, jogos):
    for j in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    lista.insert(i, jogo[:])
    jogo.clear()

print(f'-=-=-=  SORTEANDO {jogos} JOGOS  -=-=-=')
for i in range(0, jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {lista[i]}')
print('-=-=-=  BOA SORTE!  -=-=-=')
