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
      cont += 1
    if cont >= 6:
      break
lista.sort()
jogos.append(lista[:])
lista.clead()
tot += 1

'''
DESAFIO 088
EXERCÍCIO 087: Mais Sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
