# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
lista_jogos = []
qtnd = int(input('Quantos jogos você quer gerar? '))

for jg in range (0,qtnd):
    jogo = []
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            jogo.append(numero)
        if len(jogo) == 6:
            break
    lista_jogos.append(jogo)

print('-'*20)
for i in range(0,len(lista_jogos)):
    print(f'Jogo #{(i+1):>2}: {sorted(lista_jogos[i])}')
print('-'*20)