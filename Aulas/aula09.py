frase = 'Curso em Vídeo Python'

# fatiamento
print(frase[9])
print(frase[9:13])
# print(frase[9:13[)
print(frase[3:15:2])

# Análise
print(len(frase))
print(frase.count('o', 0, 15))
print(frase.find('deo'))

# Divisão
dividido = frase.split()
print(dividido[0])
print(dividido[-1])

print(''.join(dividido))
