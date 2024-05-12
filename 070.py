total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    total += preco
    if preco > 1000:
        totmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R$ {total:.2f}')
