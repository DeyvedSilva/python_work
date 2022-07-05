from random import randint
acertou = False
cont = 0
pc = randint(0, 10)
chute = 0
while not acertou:
    chute = int(input('Qual foi o número escolhido: '))
    cont += 1
    if chute == pc:
        print('\033[34mParabéns você ganhou\033[m e precisou de \033[31m{} tentativas\033[m.'.format(cont))
        acertou = True
    else:
        print('Errou! Tente novamente.')
