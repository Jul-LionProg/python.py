while True:
    n = int(input('quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11): 
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('TABUADA ENCERRADA.')



# DESAFIO 067 (Aula 15)

'''Faça um programa que mostre a TABUADA de varios valores um de cada vez
para cada valor digitado pelo usuario. O programa sera interrompido
quando o numero for NEGATIVO.'''
