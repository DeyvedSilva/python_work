tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número: [entre 0 e 20] '))
    sair = ' '
    if 0 <= num <= 20:
        print(f'O número digitado foi {tupla[num]}')
        while sair not in 'SN':
            sair = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
