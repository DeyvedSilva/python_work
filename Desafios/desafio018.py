import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo {} tem como seno {:.2f}, cosseno {:.2f} e a tangente {:.2f}.'.format(angulo, seno, coss, tang))
