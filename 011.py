larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg*alt
print('Sau parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, voce precisara de {}L de tinta'.format(tinta))
