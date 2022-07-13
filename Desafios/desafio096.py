def area(largura, comprimento):
    area_ret = largura * comprimento
    print(f'A área de um terreno {largura:.1f} x {comprimento:.1f} é de {area_ret:.1f} m²')


print('Controle de terrenos')
print('-' * 15)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
