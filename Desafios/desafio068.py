from random import randint
ganhou = 0
while True:
    print('-=' * 13)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 13)
    num = int(input('Diga um valor: '))
    palpite = ''
    while palpite not in 'PI':
        palpite = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(0, 10)
    total = num + pc
    print('-' * 40)
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {num} e o computador {pc}. Total de {total} DEU {resultado}')
    print('-' * 40)
    if palpite == 'P' and resultado == 'PAR':
        print('Você \033[34mGANHOU\033[m!')
        ganhou += 1
    else:
        print('Você \033[31mPERDEU\033[m!')
        break
print('-=' * 17)
print(f'GAMER OVER! Você venceu {ganhou} vezes.')
