expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão esta válida!')
else:
    print('Sua expressão está errada!')



'''
DESAFIO 083
Crie um programa onde o usuario digite uma
'''
