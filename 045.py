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
print('Computador JOGA {}'.format(itens[computador]))
print('Jogador JOGOU {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # PC joga Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
       print('jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Invalida')
elif computador == 1: # Computador Jogou Papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Invalida')
elif computador == 2: # Computador jogo Tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print(' Jogada Invalida')


    
    
# DESAFIO 045 (Aula 012)
# Crie um programa que faça o computador jogar JOKENPO com  VC.
  
