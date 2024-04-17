soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor' .format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {} numero PARES e a soma foi {}'.format(cont, soma))


# DESAFIO 050 (Aula 013)
# Desenvolva um programa que leia 6 numeros int e mostre a soma apenas daqueles que forem PAR. Se o valor for IMPAR. Desconsidere.
