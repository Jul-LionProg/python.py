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


