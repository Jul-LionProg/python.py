valores = []
while True:
  valores.append(int(input('digite um valor: ')))
  resp = str(input('Quer continuar [Y/N]? '))
  if resp in 'Nn':
      break
print('-=' * 30)
print(f'Voce digite {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f'Os valor em ordem decrescente são {valores}.')
if 5 in valores:
  print('O valor 5 faz parte da linha!')
else:
  print('O valor 5 não foi encontrado na lista!')
  
