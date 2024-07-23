from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

'''
DESAFIO 091:
Crie um programa nde 4 jogadores joguem um dado e tenham resultado aleatorios. Guarde esses resultdos em um
dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.
'''
