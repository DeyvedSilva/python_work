nome = str(input('Digite o seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[-1]))
