from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar:
    [ 2 ] Multiplicação:
    [ 3 ] Maior: 
    [ 4 ] Novos números:
    [ 5 ] Sair:''')
    op = int(input('>>>> Qual é sua opção: '))
    if op == 1:
    soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif op == 2:
        multi = n1 * n2
