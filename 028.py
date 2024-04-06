from random import randint
from time import sleep
computador = randint(0, 6) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entra 0 e 6. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei?')) # Jogador tentar adivinhar o numero
print('PROCESSANDO....')
sleep(4) # segundos de espera....
if jogador == computador:
    print('PARABNES!! Vocé conseguiu me vencer!')
else:
    print('GANHEI!! Eu pensei no número {} e não no {}!'.format(computador, jogador))




# DESAFIO 028 (aULA 010)]
# Escreva um programa que faça o computador "pensar em um n´umero inteiro entra" 0 e 6
# E peça o usuario tentar descobrir qual foi o número escolhido pelo computador.
# O programa devera escrever na tela se o usuaio VENCEU ou PERDEU.
