nota1 = float(input('Primeiro nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a media do aluno é {:.1f}'.format(nota1, nota2, media))
if  7 > media >= 5:
    print('O aluno esta em RECUPERAÇÃO. ')
elif media >= 5:
    print('O aluno esta REPROVADO')
elif media >= 7:
    print('O aluno esta APROVADO')


# DESAFIO 040 (aLUNA 012)
# Crie um programa qeu leia duas notas de um alunoa e calcule sua media mostrando uma mensagem no final de acordo co a madia atinginda:
''' - Media abaixo de 5.0: REPROVADO
    - Media entre 5.0 e 6.9: RECUPERAÇÃO
    - Media 7.0 ou superior: APROVADO'''
