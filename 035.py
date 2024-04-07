print('-=-' *20)
print('Analissando de Triangulo')
print('-=-' *20)
r1 = float(input('Segmento 1'))
r2 = float(input('Segmento 2'))
r3 = float(input('Segmento 3'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('Os Segmentos acima Podem Forma Um Triangulo! ')
else:
    print('Os Segmentos acima NÂO Podem Forma um Triangulo!')


# DESAFIO 035 (Aula 010)
# Desenvolva um programa que leia o comprimento de tres retas e digga ao usuario se elas podem ou não formar um triangulo.
