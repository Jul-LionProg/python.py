nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em mausculo é {}'.format(nome.upper()))
print('Seu nomeem minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu nome tem ao todo {} letras'.format(nome.find(' ')))
separa = nome.split()


# DESAFIO 022  (Aula 09)
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# *O nome com todas as letras mausculas e minusculas.
# *Quantas letras ao todo (sem considerar espaços).
# *Quantas letras tem o primeiro nome.
