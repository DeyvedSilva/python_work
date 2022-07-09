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
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')
