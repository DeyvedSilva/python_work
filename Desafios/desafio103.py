def ficha(n='', g=''):
    if n == '':
        n = '<dsconhecido>'
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(nome, gols)
