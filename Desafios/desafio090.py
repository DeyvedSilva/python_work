escola = {}
escola['Nome'] = str(input('Nome: '))
escola['Média'] = float(input(f'Média de {escola["Nome"]}: '))
if escola['Média'] >= 7:
    escola['Situação'] = 'Aprovado'
else:
    escola['Situação'] = 'Reprovado'
for k, v in escola.items():
    print(f'{k} é igual a {v}')
