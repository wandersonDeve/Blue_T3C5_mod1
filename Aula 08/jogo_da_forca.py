#3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

from random import randint

lista = ['madrugada','cientista de dados','professores','desenvolvedor full stack','ensino a distancia']
letras_escolhidas = [' ']
indice = randint(0,len(lista)-1)
tentativas = 7
print('==== JOGO DA FORCA ====')

while tentativas > 0:
    for i in lista[indice]:
        if i != ' ':
            if i in letras_escolhidas:
                print(f'{i}',end='')
            else:
                print(f'_',end='')
        else:
            print(' ',end='')

    print()

    letras_corretas = 0
    for i in lista[indice]:
        if i in letras_escolhidas:
            letras_corretas += 1
    if letras_corretas == len(lista[indice]):
        break
    print(f'A palavra tem {len(lista[indice])} letras')
    print('\033[01;35m=-\033[m'*20)
    letra = str(input('Escolha uma letra: ').strip().lower())
    if letra in letras_escolhidas:
        print(f'\033[01;38;31mVocê Ja digitou essa letra antes\033[m ---> \033[01;32m{letras_escolhidas[1:]}\033[m')
        print('\033[01;35m=-\033[m'*20)
    else:
        letras_escolhidas.append(letra)
    if letra[0] not in lista[indice]:
        tentativas -= 1
        print(f'\033[01;31mLETRA ERRADA!! você ainda tem {tentativas} tentatitas\033[m')

if tentativas == 0:
    print('\033[01;31mVOCÊ PERDEU\033[m')
else:
    print(f'\033[01;32mPARABENS\033[m a palavra era \033[01;34m{lista[indice].upper()}\033[m')