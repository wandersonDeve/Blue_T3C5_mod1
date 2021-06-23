# 6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve 
# receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só.

alunos = []
for i in range(0,15):
    aluno = {}
    notas = []
    print('__'*25)
    aluno['Nome'] = str(input('Qual o Nome do aluno: ').strip().capitalize())
    for i in range(1,6):
        notas.append(float(input(f'Qual a {i}ª nota: ').replace(',','.').strip()))

    aluno['Notas'] = notas

    if sum(notas)/len(notas) >= 7:
        aluno['Situação'] = 'Aprovado'
    elif 5 < sum(notas)/len(notas) < 6.9:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'

    alunos.append(aluno)

print('-='*25)
for i in alunos:
    for k,v in i.items():
        print(f'{k} é igual a \033[1;32m{v}\033[m')
    print('-='*25)