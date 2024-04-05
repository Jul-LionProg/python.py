'''num =  int(input('Informe um numero: '))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Milhar: {}'.format(n[0]))
print('Centena: {}'.format(n[1]))
print('Dezena: {}'.format(n[2]))
print('Unidade: {}'.format(n[3]))'''

num =  int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
