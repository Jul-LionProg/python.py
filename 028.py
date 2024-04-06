from random import randint
from time import sleep
computador = randint(0, 6) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entra 0 e 6. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei?')) # Jogador tentar adivinhar o numero
print('PROCESSANDO....')
