from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIN')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

# DESAFIO 041 (Aula 012)
# A confederação Nacional de Nataçaõ preciso de um programa que leia o anos de nascimento de um atlteta e mostre sua categoria de acordo com sua idade:
'''  - Ate 9 anos: MIRIN             - Ate 19 anos: JUNIOR
     - Ate 14 anos: INFANTIL         - Ate 25 anos: SENIOR
     - Acima: MASTER '''
