print('-' *30)
print('Sequncia de Fibonacci')
print('-' *30)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('~' *30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2   # passar a ser
    t2 = t3   # passar a ser
    cont += 1
print(' → FIM')
print('~' *30)


# DESAFIO 063  (Aula 14)
