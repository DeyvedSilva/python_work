sexo = input('Qual o sexo da pessoa? [M/F] ').strip()[0]
while sexo not in 'MmFf':
    sexo = input('Dado inválido. Informe o sexo: ')
