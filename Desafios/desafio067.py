while True:
    num = int(input('Informe um número: '))
    print('-=' * 7)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 15)
