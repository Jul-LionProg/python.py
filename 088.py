from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('   JOGA NA MGA SENA   ')
print('-' * 30)
quant = int(input('Quantos jogos voce quer que eu sorteie?'))
tot = 1
while tot <= quant:
  cont = 0
  while True:
    num = randint(1, 60)
    if num not in liste:
      liste.append(num)      
