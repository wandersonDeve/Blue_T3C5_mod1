# #04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
# 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
# palpites diga ao jogador se o número do computador é maior ou menor ao que ele
# digitou,no final mostre quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0,10)
ten = 1

print('Ola humano, vou pensar em um numero tente adivinhar.')

player = int(input('O numero que pensei entre 0 e 10 foi: ').strip())

while player != pc:
    if pc > player:
        print('Pensei em um numero maior')
    else:
        print('pensei em um numero menor')
    player = int(input('Tente novamente: '))
    ten += 1
print(f'\033[1;35mPARABENS HUMANO\033[m, Você acertou !!!\nMas precisou de {ten} tentativas')