import math

c_oposto = float(input('Comprimento do cateto oposto: '))
c_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(c_oposto, 2) + math.pow(c_adjacente, 2))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
