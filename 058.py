from random import randint
pc = randint(0, 10)
print('Bora brincar? Acabei de pensar em um numero de 0 a 10')
print('Sera que voce consegue adivinhar?')
acertou = False
palpite = 0
while not acertou: # enquato
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais!')
        elif jogador > pc:
            print('Menos!')
print('Acertou Com {} tentativas. Parabens'.format(palpite))



# DESAFIO 058 ( Aula14) mundo 2
# Melhore o jogo do DESAFIO 028 onde o pc vai pensar em um numero de 0 a 10.
# So que agora o jogador vai tentar adivinhar ate acertar mostrando no final quantas tentativas foram necessarias.
