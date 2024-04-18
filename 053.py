frase = str(input('Frase: ')).strip().upper() #.strip(eliminar os espaço antes e depois)
palavras = frase.split()   #.split(separa o vetor todo em uma lista)
junto = ''.join(palavras)  #.join(juntar tudo em uma string só)
inverso = ''
