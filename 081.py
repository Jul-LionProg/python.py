valores = []
while True:
  valores.append(int(input('digite um valor: ')))
  resp = str(input('Quer continuar [Y/N]? '))
  if resp in 'Nn':
      break
print('-=' * 30)
