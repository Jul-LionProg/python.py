jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogaodr: '))
tot = int(input(f'Quantas partidas {jogoador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   quantos gols na partidas {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
