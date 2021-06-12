### 4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0,10)
tentativas = 0

print('Pensei em um numero de 0 a 10.')

while True:
    jogador = int(input('Adivinhe que numero pensei: ').strip())
    tentativas += 1
    if jogador == pc:
        break
    else:
        print('\033[01;31mVocê errou, tente novamente.\033[m')

print(f'\033[01;34mPARABENS\033[m pensei no numero {pc}, você acertou em {tentativas} tentativas')