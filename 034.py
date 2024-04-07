salario = float(input('Qual é o salaŕio do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) # Para usar desconto usa -
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))




# DESAFIO 034 (aula 010)
# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores a 1.250,00 calcule um aumento de 10%.
# Para salários inferior ou iguais, o aumento é de 15%.
