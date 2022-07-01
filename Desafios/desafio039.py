from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year
idade = int(ano_atual - ano)
if idade < 18:
    print('Ainda vai se alistar. Falta {} anos.'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print('Já passou do tempo do alistamento. Passou {} anos.'.format(idade - 18))
