numero = str(input('Digite um número entre 0 e 9999: ')).strip()
tamanho = len(numero)

print('Unidade: {}'.format(numero[3:]))
print('Dezena: {}'.format(numero[2:-1]))
print('Centena: {}'.format(numero[1:-2]))
print('Milhar: {}'.format(numero[:-3]))
