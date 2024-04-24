somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip() # tirar os espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade # somar tdas as idades do grupo
