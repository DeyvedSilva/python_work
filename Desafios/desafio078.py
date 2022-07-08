lista = list()
maxi = list()
mini = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=' * 30)
for p, v in enumerate(lista):
    if v == max(lista):
        maxi.append(p)
    elif v == min(lista):
        mini.append(p)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições {maxi}')
print(f'O menor valor digitado foi {min(lista)} nas posições {mini}')
