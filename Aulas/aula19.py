dados = dict()
dados = {'Nome': 'Pedro', 'Idade': 25}
print(dados['Nome'])
dados['Sexo'] = 'M'
del dados['Idade']
print(dados)

filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whndon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[0]['titulo'])

pessoas = {'nome': 'Deyved', 'Sexo': 'M', 'idade': 36}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

