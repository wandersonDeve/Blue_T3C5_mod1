#03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import datetime

menor_de_idade = maior_de_idade = 0
for i in range(1,8):
    ano_nas = int(input(f'Digite seu ano de nascimento da {i}ª pessoa: ').strip().replace(',','.'))
    idade = datetime.today().year - ano_nas
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f'Com os anos indicados temos {maior_de_idade} pessoas maiores de idade e {menor_de_idade} menores de idade')