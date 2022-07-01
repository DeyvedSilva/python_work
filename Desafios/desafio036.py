valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você deseja pagar? '))
valor_maximo = salario * 0.3
mensalidade = valor / (anos * 12)
if mensalidade > valor_maximo:
    print('Empréstimo negado.')
else:
    print('Parabéns, empréstimo aprovado!!!')
    print('O valor da prestação mensal será R${:.2f}'.format(mensalidade))
