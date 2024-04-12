r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
       print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
    print('ESCALENDO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima não PODEM FORMAR triangulo')



# DESAFIO 042 (Aula 012)
# Refaça o DESAFIO 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
'''- ESCALENDO:
   - ISOSCELES:
   - EQUILATERO:'''
