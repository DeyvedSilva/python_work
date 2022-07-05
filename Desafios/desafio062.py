termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = total = 0
sair = 10
while cont < sair:
    termo_novo = termo + total * razao
    cont += 1
    total += 1
    print(termo_novo, end=' -> ')
    if cont == sair:
        print('PAUSA')
        sair = int(input('Quantos termo você quer ver? '))
        cont = 0
print('Progressão finalizada com {} termos mostrados.'.format(total))
