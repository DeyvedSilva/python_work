total_gasto = produto_1000 = valor_barato = cont = 0
produto_barato = ' '
print('=' * 30)
print('SUPER BARATÃO'.center(30))
print('=' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total_gasto += preco
    if cont == 0 or preco < produto_barato:
        valor_barato = preco
        produto_barato = produto
    cont += 1
    if preco > 1000:
        produto_1000 += 1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print(' FIM DO PROGRAMA '.center(30, '-'))
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {produto_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${valor_barato:.2f}')
