num = int(input('Digite um número inteiro: '))
escolha = int(input("""Escolha qual será a base de conversão:
   1 para binário
   2 para octal
   3 para hexadecimal
   """))
if escolha == 1:
    print('O número {} convertido em binário é {}.'.format(num, bin(num)))
elif escolha == 2:
    print('O número {} convertido para octal é {}.'.format(num, oct(num)))
elif escolha == 3:
    print('O número {} convertido em hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Opção inválida!')
