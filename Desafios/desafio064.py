cont = soma = 0
valor = int(input('Digite um valor: '))
while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite um valor: '))
print('Foram digitados {} números e a soma entre eles foi {}.'.format(cont, soma))
