casa  = float(input('Valor da casa: R$'))
salario = float(input('salario de comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestaçao = casa / (anos * 12)
minino = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos),end='')
if prestaçao <= minino:
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')


# DESAFIO 036 (Aula 012)
# Escreva um programa para aprovar o emprestimo bancario pra a compra de uma casa.
# Pergutne o Valor da casa o salario do comprador e em quanto anos ele vai pagar.
# Aprestação mensal não pode exceder 30% do salario ou então o emprestimo sera negado.
