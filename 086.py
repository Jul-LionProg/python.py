matriz = [[0, 0, 0],[0, 0,0],[0, 0, 0]]
for l in range(0, 3):
    for c  in range(0, 3):
        matriz[l][c] = int(inputt(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
