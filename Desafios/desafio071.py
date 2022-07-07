print('~' * 30)
print(' BANCO CEV '.center(30, '-'))
print('~' * 30)
valor = int(input('Que valor você quer sacar? R$'))
ced_50 = valor // 50
valor -= ced_50 * 50
ced_20 = valor // 20
valor -= ced_20 * 20
ced_10 = valor // 10
valor -= ced_10 * 10
ced_1 = valor // 1
if ced_50 != 0:
    print(f'Total de {ced_50} cédulas de R$50')
if ced_20 != 0:
    print(f'Total de {ced_20} cédulas de R$20')
if ced_10 != 0:
    print(f'Total de {ced_10} cédulas de R$10')
if ced_1 != 0:
    print(f'Total de {ced_1} cédulas de R$1')
print('=' * 30)
