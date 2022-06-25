# Exercício 006
import math
num = int(input('Digite um número: '))
print('Você digitou {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(num, num * 2, num * 3, math.sqrt(num)))

# outras possibilidades
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, pow(num, 1/2)))
