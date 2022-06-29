cidade = str(input('Digite o nome de uma cidade: ')).strip()
nome = cidade.lower().split()
print('O nome da cidade começa com "SANTO" {}'.format('santo' in nome[0]))
