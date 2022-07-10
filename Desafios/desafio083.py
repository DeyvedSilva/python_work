expr = str(input('Digite a expressão: ')).strip()
lista = []
for c in expr:
    lista.append(c)
if lista.count('(') == lista.count(')') and lista.index('(') < lista.index(')'):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
print(lista.index('(') < lista.index(')'))
