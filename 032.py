from datetime import date # Pesquisar a data e hora do seu pc atual (date) só pesquisa a data
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NAO é BISSEXTO'.format(ano))
 

 # DESAFIO 032 (Aula 010)
 # Faça um programa que leia um ano qualquer e mostre se ele é BISEXTO.
 
