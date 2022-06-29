import random

num = random.randint(0, 5)
chute = int(input('Pensei em um número. Tenta advinhar qual foi entre 0 e 5: '))
if chute == num:
    print('Parabéns, você venceu!')
else:
    print('Perdeu! O número foi {}'.format(num))
