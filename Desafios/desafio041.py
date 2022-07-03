from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Com {} anos. Sua categoria é \033[34mMirim\033[m.'.format(idade))
elif idade <= 14:
    print('Com {} anos. Sua categoria é \033[34mInfantil\033[m.'.format(idade))
elif idade <= 19:
    print('Com {} anos. Sua categoria é \033[33mJunior\033[m.'.format(idade))
elif idade <= 25:
    print('Com {} anos. Sua categoria é \033[32mSênior\033[m.'.format(idade))
else:
    print('Com {} anos. Sua categoria é \033[31mMaster\033[m.'.format(idade))
