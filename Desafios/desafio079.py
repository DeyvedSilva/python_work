lista = []
while True:
    num = int(input('Digite uma valor: '))
    if len(lista) == 0:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        for c in lista:
            if num == c:
                print('Valor duplicado! Não vou adicionar...')
                break
            elif c == lista[-1]:
                lista.append(num)
                print('Valor adicionado com sucesso...')
                break
    continuar = str(input('Quer continuar: [S/N] ')).strip().lower()[0]
    lista.sort()
    while continuar not in 'sn':
        continuar = str(input('Valor inválido! Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('~=' * 30)
print(f'Você digitou os valores {lista}')
