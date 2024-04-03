salário = float(input('Qual é o salário do Funcionario? R$:'))
novo = salário + (salário * 30 / 100)
print('Um funcionario que ganhava R${:.2f}, com 30% de aumento, passa a receber R${:.2f}'.format(salário, novo))
