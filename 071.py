print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
