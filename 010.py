real  = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.13
euro  = real / 5.42
pesos = real / 0.015
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))
print('Com RS{:.2f} voce pode comprar EUR${:.2f}'.format(real, euro))
print('Com R${:.2f} voce pode comprar ${:.2f}'.format(real, pesos))
