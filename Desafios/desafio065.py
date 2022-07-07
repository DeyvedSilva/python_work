cont = soma = maior = menor = 0
sair = ''
while sair != 'S':
    num = int(input('Digite um valor inteiro: '))
    if cont == 0:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    soma += num
    cont += 1
    sair = input('Você deseja sair? [S/N] ').strip().upper()[0]
media = soma / cont
print('A média foi {:.2f}, o maior é {} e o menor é {}.'.format(media, maior, menor))

