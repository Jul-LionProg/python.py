from random import randint
from time  import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Sua opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador =  int(input('Qual é a sua jogado?'))
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('POO!')
print('-=' * 11)
