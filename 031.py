distancia = float(input('Qual é a distancia da sua viagem? '))
print('Vocẽ esta preste a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia *0.45 # + Pratico e resumindo
'''if distancia <= 200:
     preço = distancia * 0.50
   else:
     preço = distancia * 0.45'''
