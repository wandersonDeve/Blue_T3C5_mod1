# #05 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos
# são informados por meio de código.
# Os códigos utilizados são:
# 1 , 2, 3 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - José / 2- João / etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
#         O total de votos para cada candidato;
#         O total de votos nulos;
#         O total de votos em branco;
#         A percentagem de votos nulos sobre o total de votos;
#         A percentagem de votos em branco sobre o total de votos.

from random import randint, uniform
Joao = jose = maria = pedro = nulo = branco = total_votos = 0


for i in range(1,7):
    if i == 1:
        joao = randint(0,10)
        total_votos += joao
    elif i == 2:
        jose = randint(0,10)
        total_votos += jose
    elif i == 3:
        maria = randint(0,10)
        total_votos += maria
    elif i == 4:
        pedro = randint(0,10)
        total_votos += pedro
    elif i == 5:
        nulo = randint(0,10)
        total_votos += nulo
    elif i == 6:
        branco == randint(0,10)
        total_votos += branco
um_perc = total_votos/100

print(f'Tivemos um total de {total_votos} votos,\nSendo eles:\n{joao} Votos para o Joao\n{jose} Votos para o Jose\n{maria} Votos para o Maria\n{pedro} Votos para o Pedro\n{nulo*um_perc:.2f} % de Votos Nulos\n{branco*um_perc:.2f} % de Votos Brancos')