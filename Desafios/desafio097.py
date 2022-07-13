def escreva(txt):
    tam = len(txt) + 2
    print('~' * tam)
    print(txt.center(tam))
    print('~' * tam)


texto = str(input('Informe uma mensagem: ')).strip()
escreva(texto)
