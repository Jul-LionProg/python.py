from random import choice
n1 = str(input('Primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('Treceiro aluno:'))
n4 = str(input('quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi VC{}'.format(escolhido))