pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

teste = list()
teste.append('Deyved')
teste.append(36)
galera = list()
galera.append(teste[:])  # atribui valores sem fazer correspondência entre as listas
print(teste, galera)
galera_nova = list()
galera_nova.append(teste)  # faz uma correspondência entre as duas listas
teste[0] = 'Maria'
teste[1] = 22
print(teste, galera, galera_nova)

galera = list()
dado = list()
total_maior = total_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
print(f'{total_maior} são maiores de idade e {total_menor} são menores de idade.')

for i in galera:
    print(i)
