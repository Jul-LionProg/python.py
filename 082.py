num =  list()
pares = list()
impares = list()
while = True:
  num.append(int(imput('Digite um numero: ')))
  resp = str(input('quer continuar [N/Y]'))
  if resp in 'nN':
    break
for i, v in enumerate(num):
  if v % 2 == 0:
    pares.append(v)
  elif v % 2 == 1:
        impares.append(v)
print('-= *' 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
