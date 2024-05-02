print('Gerador de PA')
print( '-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de  PA: '))
termo = primeiro
cont = 1
while cont <= 10: # laço
   print('{} ➙ '.format(termo),end='')
    termo += razao
