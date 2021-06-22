# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

aluno = {}
aluno['Nome'] = str(input('Qual o Nome do aluno: ').strip().capitalize())
aluno['Media'] = float(input('Qual a sua media: ').replace(',','.').strip())

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 < aluno['Media'] < 6.9:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('-*'*30)
for k,v in aluno.items():
    print(f'{k} é igual a {v}')