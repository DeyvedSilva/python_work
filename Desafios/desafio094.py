pessoas = {}
populacao = []
soma = 0
sair = True
while True:
    pessoas["nome"] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
        if pessoas['sexo'] in 'FfMm':
            break
        print('ERRO! Por favor, apenas digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    populacao.append(pessoas.copy())
    pessoas.clear()
    while True:
        sair = str(input('Quer sair? [S/N] ')).strip()[0]
        if sair in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if sair in 'Ss':
        break
print('-=' * 30)
media = soma / len(populacao)
print(f'- O grupo tem {len(populacao)} pessoas')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram ', end='')
for p in populacao:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('A lista das pessoas que estão acima da média:')
for p in populacao:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')

