from datetime import datetime
dados = dict()
dodas['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['cpts'] != 0:
  dados['contratação'] = int(input('Ano de contratação: '))
  dados['salario'] = float(input('Salario: R$ '))
  dados['aponsentadoria'] = dados['idade'] + ((dados[contratação] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
