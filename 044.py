preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/Pix
[ 2 ] Á vita no cartão
[ 3 ] 2x no cartão S/juros
[ 4 ] 3x ou mais C/juros''')
opçao = int(input('Qual a forma de pagamanto? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas Parcelas? '))
    parcela = total / totalparc
   print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no fi'.format(preço, total))



# DESAFIO 044 (Aula 012)
# Elabore um programa que calcule o valor a ser pago pro um produto. Considerando o seu preço normal e condição de pagamento:
'''- A vista dinherio / pix:       
   - Em ate 2x no cartão: normal 10% de desconto
   - 3x ou mais no cartão: 20% de juros
   - A vista no cartão: 5% de desconto.'''
