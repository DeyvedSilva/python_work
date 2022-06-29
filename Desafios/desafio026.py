frase = str(input('Digite uma frase: ')).strip()
print('Quantas vezes aparece a letra "A": {}'.format(frase.upper().count('A')))
print('Em qual posição ela aparece primeiro: {}'.format(frase.upper().find('A') + 1))
print('Em qual posição ela aparece a última vez: {}'.format(frase.upper().rfind('A') + 1))
