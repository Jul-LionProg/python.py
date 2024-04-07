salario = float(input('Qual é o salaŕio do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) # Para usar desconto usa -
else:
