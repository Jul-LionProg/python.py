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
