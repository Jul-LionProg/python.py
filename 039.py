from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
     print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    anos = atual - saldo
    print('Seu alistamento foi em {}'.format(anos))
 

    
    
# DESAFIO 039 (Aula 012)
# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
# Se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se ja passou do tempo do alistamento
# Seu programa tambem devera mostra o tempo que falta ou que passou do prazo.
