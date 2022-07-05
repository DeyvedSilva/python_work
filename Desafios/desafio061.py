termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 0
while cont < 10:
    termo_novo = termo + cont * razao
    cont += 1
    print(termo_novo, end=' -> ')
print('Fim')
