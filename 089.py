ficha = list()
while True:
  nome = str(input('Nome: ')
  nota1 = flaot(input('Nota 1: '))
  nota2 = flaot(input('Nota 2: '))
  media = (nota1, nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = str(input('Quer continuar [S/N]? ')
  if resp in 'Nn':
      break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a  in enumerate(ficha)
