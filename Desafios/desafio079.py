lista = []
while True:
    num = int(input('Digite uma valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar: [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Valor inválido! Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('~=' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')
