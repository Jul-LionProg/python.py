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
        print('{} x {} = {}'.format(n1, n2, multi))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
        print('Entre {}, e {}, o maior é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Numero Novo: ')
        n1 = int(input('Primerio numero: '))
        n2 = int(input('Segundo numero: '))
    elif op == 5:
        print('Finalizando....')
    else:
        print('Opção invalida. ')
    print('=-=' * 10)
    sleep(2)
    print('Fim do programa!')
    
    
    
# DESSAFIO 059 (Aula 014)
'''Crie um progrma que leia dois valores e mostre um menu
    [ 1 ]SOMA
    [ 2 ]MULTIPLICAÇÃO
    [ 3 ]MAIOR QUE
