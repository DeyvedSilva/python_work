dias = int(input('Foram quantos dias alugados: '))
km = float(input('Quantos quilometros foram rodados: '))
total = 60 * dias + 0.15 * km
print('O valor total que será pago é R${:.2f}'.format(total))
