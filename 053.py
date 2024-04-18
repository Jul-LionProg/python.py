frase = str(input('Frase: ')).strip().upper() #.strip(eliminar os espaço antes e depois)
palavras = frase.split()   #.split(separa o vetor todo em uma lista)
junto = ''.join(palavras)  #.join(juntar tudo em uma string só)
inverso = ''
for letra in range(len(junto)-1, -1, -1): # len foi da ultima letra ate a -1 primeria pulando um -1
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALINDROMO:')
else:
    print('A frase digitada NÃO é um PALINDROMO')
