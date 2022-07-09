cont = 0
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    sair = str(input('Deseja sair? [S/N] '))
    if sair in 'Ss':
        break
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
