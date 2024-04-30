'''USANDO
from math import factorial
n = int(input('Calcule o fatorial de: '))
f = factorial
print('O fatorial de {} é {}.'.format(n, f))'''


n = int(input('Calcule o fatorial de: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))


#DESAFIO 060 (Aula 14)
# Faça um progrma que leia um numero e mostre seu FATORIAL.
# 5! = 5 x 4 x 3 x 2 x 1 = 120
