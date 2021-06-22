# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

cad = []
idade = 0

while True:
    pessoas = {}
    pessoas['Nome'] = str(input('Qual o nome: '))
    pessoas['Sexo'] = str(input('Qual o sexo: ')).upper()
    pessoas['Idade'] = int(input('Qual a Idade: '))
    idade += pessoas['Idade']
    cad.append(pessoas)
    ctrl = str(input('Deseja continuar: [S/N]' )).upper()
    if ctrl in 'Nn':
        break

media = idade/len(cad)
print('=-'*20)
print(f'Foram cadastradas {len(cad)} pessoas\n')
print(f'A media da idade do grupo foi de {media:.2f}')

print('As melhures cadastradas foram: ',end=' ')
for i in range(0,len(cad)):
    if cad[i]['Sexo'] == 'F':
        print(cad[i]['Nome'], end=' ')
print()

print('As pessoas com idade maior que a media são: ',end=' ')
for i in range(0,len(cad)):
    if cad[i]['Idade'] > media:
        print(cad[i]['Nome'],end=' ')
