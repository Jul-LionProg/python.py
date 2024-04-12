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
