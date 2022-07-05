soma_idade = 0
velho = ''
idade_velho = 0
mulheres = 0
for a in range(1, 5):
    print('----- {}ª Pessoa -----'.format(a))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower().strip()
    soma_idade += idade
    if a == 1:
        if sexo == 'm':
            velho = nome
            idade_velho = idade
        elif sexo == 'f':
            if idade < 20:
                mulheres += 1
    elif sexo == 'm' and idade > idade_velho:
        velho = nome
        idade_velho = idade
    elif sexo == 'f' and idade < 20:
        mulheres += 1
print('A média de idade do grupo é {:.2f} anos;'.format(soma_idade / 4))
print('O homem mais velho tem {} anos e se chame {};'.format(idade_velho, velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
