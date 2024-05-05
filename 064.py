num = cont = soma = 0 # pode resumir tudo em uma linha
num = int(input('Digiteu um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou  {} numeros e a soma entre eles foi {}.'.format(cont, soma))



# DESAFIO 064  (Aula 14)
# Crie um progroma qie leia varios numeros inteiros pelo teclado.
