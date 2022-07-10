lista = []
lista_impar = []
lista_par = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    sair = str(input('Deseja sair? [S/N] '))
    if sair in 'Ss':
        break
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')
