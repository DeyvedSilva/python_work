nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota2 + nota1) / 2

if media < 5.0:
    print('Sua média é {} e você foi \033[31mREPROVADO\033[m.'.format(media))
elif media < 6.9:
    print('Sua média é {} e você está em \033[33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('Sua média é {} e você foi \033[32mAPROVADO\033[m.'.format(media))
