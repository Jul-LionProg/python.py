num = int(input('Digite um numero inteiro:'))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente:')
  
