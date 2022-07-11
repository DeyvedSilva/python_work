lista_completa = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista_completa.append([nome, [nota1, nota2], media])
    sair = str(input('Quer sair: [S/N] ')).strip()[0]
    if sair in 'Ss':
        break
print('-=' * 33)
print(f'{"Nº":<4}{"Nome":<10}{"Média":<8}')
print('-' * 22)
for i, a in enumerate(lista_completa):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-' * 30)
    escolha = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if escolha == 999:
        break
    if escolha <= len(lista_completa) - 1:
        print(f'Notas de {lista_completa[escolha][0]} são {lista_completa[escolha][1]}')
