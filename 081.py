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
