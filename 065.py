resp = 'S'
soma = quant = maior = menor = 0
while resp in 'Ss':  # entre
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1 
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [N/S] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numero e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



# DESAFIO 065 (Aula 14)
# Crie um programa que leia varios numeros inteiros pelo teclado.
# NO final da execução mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer parar ou continu....
