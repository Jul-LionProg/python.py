a = int(input('Primeira valor:'))
b = int(input('Segundo valor'))
c = int(input('Terceiro valor'))
# Verificando quem é o menor
menor = a 
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c
# Verificando o maior preço
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O MENOR valor digitado foi {}'.format(menor))
