from random import randint


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    mai = cont = 0
    for i in range(0, len(num)):
        print(num[i], end=' ')
        cont += 1
        if mai == 0:
            mai = num[i]
        if num[i] > mai:
            mai = num[i]
    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10))
maior()
