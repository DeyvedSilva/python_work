escola = {}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
escola['Nome'] = nome
escola['Média'] = media
situacao = ' '
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
escola['Situação'] = situacao
for k, v in escola.items():
    print(f'{k} é igual a {v}')
