reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))

if reta1 < reta2 + reta3 and reta3 < reta2 + reta1 and reta2 < reta3 + reta1:
    print('As reta podem formar um triângulo.')
    if reta1 == reta3 == reta2:
        print('Triângulo \033[33mequilátero\033[m')
    elif reta1 == reta3 or reta2 == reta1 or reta2 == reta3:
        print('Triângulo \033[34misósceles\033[m.')
    else:
        print('Triângulo \033[31mescaleno\033[m.')
else:
    print('As retas não podem formar um triângulo')
