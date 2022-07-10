pessoas = list()
dados = []
cont = maior = menor = 0
pesadas = []
leves = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if cont == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    cont += 1
    pessoas.append(dados[:])
    dados.clear()
    sair = input('Quer continuar? [S/N] ').strip()[0]
    if sair in 'Nn':
        break
print('~' * 40)
print(f'Ao todo, você cadastrou {cont} pessoas')
for c in pessoas:
    if c[1] == maior:
        pesadas.append(c[0])
    elif c[1] == menor:
        leves.append(c[0])
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {pesadas}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {leves}')
