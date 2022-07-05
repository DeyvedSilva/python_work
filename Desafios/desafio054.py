from datetime import date
maior = 0
menor = 0
ano_atual = date.today().year
for a in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(a)))
    if (ano_atual - ano) >= 21:
        maior += 1
    else:
        menor += 1
print('O total de pessoas menores de idade é {} e o total de maiores de idade é {}.'.format(menor, maior))
