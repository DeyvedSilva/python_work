# definição de função
def mostralinha():
    print('-' * 30)


mostralinha()


def mensagem(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


mensagem('Sistemas de alunos')


def soma(a, b):
    s = a + b
    print(f'A soma é {s}')


soma(4, 5)
soma(8, 9)
soma(1, 2)
soma(b=3, a=2)


def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
