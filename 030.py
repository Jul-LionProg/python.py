numero = int(input('Me diga um número: '))
resultado = numero % 2  # todo resto de um numero (impar(1) ou par(0)) dividido por %2 vai dar (0 ou 1) 
if resultado == 0:
    print('O Número {} é PAR!'.format(numero))
else:
