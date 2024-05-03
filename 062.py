print('Gerador de PA')
print( '-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de  PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total: # laço
        print('{} ➙ '.format(termo),end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))


# DESAFIO 062  (Aula 14)
# Melhore o DESAFIO 061, perguntando para o usuaio se ele quer mostrar mais algum termos,
# O programa encerra quando ele disser que quer mostra o Numero
