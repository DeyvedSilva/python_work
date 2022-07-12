from datetime import date
ano_atual = date.today().year
pessoas = {'Nome': str(input('Nome: ')), 'Idade': ano_atual - int(input('Ano de nascimento: ')),
           'ctps': int(input('Carteira de trabalho (0 não tem): '))}
if pessoas['ctps'] != 0:
    pessoas['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoas['Salário'] = float(input('Salário: '))
    ano_falta = 35 - (ano_atual - pessoas['Ano de contratação'])
    pessoas['aposentadoria'] = pessoas['Idade'] + ano_falta
for k, v in pessoas.items():
    print(f'{k} tem o valor {v}')
