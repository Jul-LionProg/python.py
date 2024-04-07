salario = float(input('Qual é o salaŕio do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) # Para usar desconto usa -
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))
