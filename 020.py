from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Treceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação sera!')
print(lista)



# DESAFIO 020 (Aula 08)
# O mesmo profesor do desafior anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos alunose mostre a ordem sorteada.
