reta1 = float(input('Informe o comprimento da primeira reta: '))
reta2 = float(input('Informe o comprimento da segunda reta: '))
reta3 = float(input('Informe o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta3 < reta2 + reta1 and reta2 < reta3 + reta1:
    print('As reta podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
