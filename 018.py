''' import math
angulo = float(input('digite o Angulo que voce deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente)) '''


from math import radians, sin, cos, tan
angulo = float(input('digite o Angulo que voce deseja:'))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))



# DESEFIO 018 (aula 08)
# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno, tangente desse angulo.

# print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
