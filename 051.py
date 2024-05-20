primeiro = int(input('Primeiro Termo '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='➝ ')
print('ACABOU')



# DESAFIO 051 (Aula 013)
# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZAO de uma (PA)
# No final mostre os 10 primeiros termos dessa progressão.
# Termo = contar 0 a ....
# PA = pular de 2 em 2 ou (4 em 4) (7 em 7) etcs...
