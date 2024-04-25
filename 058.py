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
