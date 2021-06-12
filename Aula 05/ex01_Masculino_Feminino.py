### 1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valoclearres ‘M’ ou ‘F’.Caso esteja errado, peça a digitação novamente até ter um valor correto ###

while True:
    sexo = str(input('Qual o seu sexo [M,F]: ').strip().upper())
    if sexo[0] in 'MF':
        break
    else:
        print('Resposta invalida tente novamente')
if sexo[0] == 'M':
    print('Seu sexo é Masculino')
else:
    print('Seu sexo é Feminino')