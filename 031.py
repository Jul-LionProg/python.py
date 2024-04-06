distancia = float(input('Qual é a distancia da sua viagem? '))
print('Vocẽ esta preste a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia *0.45 # + Pratico e resumindo
'''if distancia <= 200:
     preço = distancia * 0.50
   else:
     preço = distancia * 0.45'''
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


# DESAFIO 031 (aula 010)
# Desenvolva um programa que pergunte a distancia de uma viagem em Km.
# Calcule o preço da passagem,cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas. 
