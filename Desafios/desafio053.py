frase = input('Digite uma frase: ').strip().upper()
lista = frase.split()
nova = ''.join(lista)
invertido = ''
for c in range(len(nova) - 1, -1, -1):
    invertido += nova[c]
print('O inverso de {} é {}'.format(nova, invertido))
if nova == invertido:
    print('Temos um palíndromo!')
else:
    print('Não é palíndromo!')
