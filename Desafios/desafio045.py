from time import sleep
from random import randint
print("""Suas opções:
1 - PEDRA
2 - PAPEL
3 - TESOURA""")
pc = randint(1, 3)
opcao = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 15)
print('Computador jogou ', end='')
if pc == 1:
    print('Pedra')
elif pc == 2:
    print('Papel')
else:
    print('Tesoura')
print('Player jogou ', end='')
if opcao == 1:
    print('Pedra')
elif opcao == 2:
    print('Papel')
else:
    print('Tesoura')
print('-=' * 15)
if opcao == pc:
    print('\033[34mEMPATE\033[m')
elif opcao == 1 and pc == 2:
    print('\033[31mCOMPUTADOR VENCEU')
elif opcao == 1 and pc == 3:
    print('\033[34mJOGADOR VENCEU')
elif opcao == 2 and pc == 3:
    print('\033[31mCOMPUTADOR VENCEU')
elif opcao == 2 and pc == 1:
    print('\033[34mJOGADOR VENCEU')
elif opcao == 3 and pc == 1:
    print('\033[31mCOMPUTADOR VENCEU')
else:
    print('\033[34mJOGADOR VENCEU')
