numeros = list()
while True:
  n = int(input('Digite um valor: '))
  if n not in numeros:
      numeors.append(n)
      print('Valor adicionado com sucesso...')
  else:
      print('Valor duplicado! Não vou adicionar...')
