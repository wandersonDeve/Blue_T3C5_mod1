# 2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".


sim = 0

def verificar_resposta(pergunta):
    while True:
        ask = str(input(pergunta).strip().lower())
        if ask[0] in 'sn':
            break
        else:
            print('Resposta Invalida')
    return ask[0]

perguntas = ['Você telefonou para a vítima? ','Você esteve no local do crime? ','Você mora perto da vítima? ','Você devia para a vítima? ','Você já trabalhou com a vítima? ']

for pergunta in perguntas:
    if verificar_resposta(pergunta) == 's':
        sim += 1

if sim == 2:
    print('Não Saia do país, pois você é um SUSPEITO')
elif 3 <= sim <=4:
    print('Você esta sendo preso como \033[1;31mCUMPLICE\033[m')
elif sim ==5:
    print('Você foi \033[1;31mCULPADO\033[m')
else:
    print('Você esta liberado, foi considerado \033[1;32mINCOCENTE\033[m')
