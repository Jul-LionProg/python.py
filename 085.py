num = [[], []]
valor = 0
for c in range(1, 8):
  valor = int(input(f'digite o {c}º valor: '))
  if valor % 2 == 0:
      num[0].append(valor)
else:
  num[0].append(valor)
print('-=' * 30)
num[0].sort()
num[0].sort()
print(f'Os valores pares dogotados foram: {num[0]}')
