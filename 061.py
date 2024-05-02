print('Gerador de PA')
print( '-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de  PA: '))
termo = primeiro
cont = 1
while cont <= 10: # laço
   print('{} ➙ '.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')


# DESAFIO 061 (Aula 014)
# Refaça o DESAFIO 051, lendo o primeiro termo ea razao de uma PA, mostrando os 10 primeiro termos da progressão usando a estrutura WHILE.
