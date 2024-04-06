velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Vocẽ excedeu o limite permitido é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Vocẽ deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenho um bom dia! Dirija com cuidado e segurança!')




# DESAFIUO 029 (Aula 010)
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem, Dizendo 
# "MULTADO".
# A multa vai custar R$7,00 por cada KM acima do limite.
