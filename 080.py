lista = []
for c in range(0, 5):
  n = int(input('Digite um valor: '))
  if c == 0 or n > lista[-1]:
      lista.append(n)
      print('Adicionado ao final da lista...')
