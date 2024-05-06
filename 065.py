resp = 'S'
soma = quant = maior = menor = 0
while resp in 'Ss':  # entre
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1 
    if quant == 1:
        maior = menor = num
    else:
