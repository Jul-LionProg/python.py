peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DE PESO normal')
elif 25 <= imc < 30:
    print('PARABENS! Voce esta na faixa de peso normal')
elif 30 <= imc < 40:
    print('Voce esta em SOBREPESO')
elif imc >= 40:


    
# DESAFIO 043 (Aula 012)
# Desenvolva um a logica que leia o peso ea altura se uma pessoa calculando o sei IMC e mostre seu status de acordo com a tabela abaixo.
'''- Abaixo de 18.5: Abaixo de peso     - 25 ate 30: Sobrepeso
   - Entre 18.5 e 25: Peso ideal        - 30 ate 40: Obesidad    - Acima de 40: Obesidade Morbida'''
