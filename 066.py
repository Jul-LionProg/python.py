soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!') # f string

# DESAFIO 066 (Aula 15)
# Crie um programa que leia varios numeros inteiros. O programa so vap para quando o usuario digitar 999, que é Aula
CONDIÇÃO DE PARADA. no final mostre quantos numeros foram digitados e qual a soma entre eles
[DESCONSIDERANDO O FLAG].
