sexo = str(input('Informe seu sexo [M/F]')).strip().upper()[0] # pegar a primeria Letra
while sexo not in 'MmFf': # enquanto
    sexo - str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))
