def leia_dinheiro(txt):
    while True:
        msg = input(txt)
        if msg.isnumeric():
            return int(msg)
        else:
            print(f'\033[31mERRO! \"{msg}\" é um preço inválido\033[m')
