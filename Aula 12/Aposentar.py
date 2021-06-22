# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
# , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
# contribuir por 35 anos para se aposentar.

from datetime import date

ano_atual = date.today().year

aposento = {}
aposento['Nome'] = str(input('Qual o seu nome: '))
ano_nascimento = int(input('Que ano você nasceu? '))
aposento['Idade'] =  ano_atual - ano_nascimento
aposento['CTPS'] = int(input('Qual o numero da sua carteira de trabalho? [0 não tem] '))

if aposento['CTPS'] != 0:
    aposento['Contratado'] = int(input('Em que ano foi contratado? '))
    aposento['Salario'] = float(input('Qual o seu salario? '))
    aposento['Aposentadoria'] = aposento['Contratado'] + 35 - ano_nascimento

for k,v in aposento.items():
    print(f'{k} tem o valor {v}')