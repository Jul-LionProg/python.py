galera = list()
pessoa = dict()
soma = media = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
