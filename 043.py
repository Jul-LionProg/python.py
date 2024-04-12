peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DE PESO normal')



# DESAFIO 043 (Aula 012)
# Desenvolva um a logica que leia o peso ea altura se uma pessoa calculando o sei IMC e mostre seu status de acordo com a tabela abaixo.
'''- Abaixo de 18.5: Abaixo de peso     - 25 ate 30: Sobrepeso
   - Entre 18.5 e 25: Peso ideal        - 30 ate 40: Obesidad    - Acima de 40: Obesidade Morbida'''
