co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = (co**2 + ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))



import math
co = float(input('Comprimento do cateto oposto: ')) 
ca = float (input('Comprimento do cateto adiacente: '))
hi = math.hypot (co, ca) 
print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
co = float(input('Comprimento do cateto oposto: ')) 
ca = float (input('Comprimento do cateto adiacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))



# DEFASIO 017  (Aula08)
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e mostre o comprimento da hipotenusa.
