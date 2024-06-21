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
