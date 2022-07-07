maiores = homens = mulheres = 0
while True:
    print('-' * 30)
    print(' CADASTRE UMA PESSOA '.center(30))
    print('-' * 30)
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres += 1
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(' FIM DO PROGRAMA '.center(30, '='))
print(f'Total de pesoas com mais de 18 anos é {maiores};')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
