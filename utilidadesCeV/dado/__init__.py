def leia_dinheiro(txt):
    while True:
        msg = str(input(txt)).replace(',', '.').strip()
        if msg.isalpha() or msg != '':
            return float(msg)
        else:
            print(f'\033[31mERRO! \"{msg}\" é um preço inválido\033[m')
