from pygame import mixer
from time import sleep
from random import randint
import os

#   TRILHA SONORA E AUDIOS DO JOGO
def audiJogo(musica,play=False):
    musicas = ['sons/typewriter.mp3','sons/caminhando_normal.mp3','sons/cachoeira.mp3']
    if play:
        mixer.init()
        mixer.music.load(musicas[musica])
        mixer.music.play(loops=10)
    else:
        mixer.music.stop()

#   FRASES DE INICIO DE ESTAGIO
def atualStage(atual):
    frases = ['Cansado da cidade você revolve vender tudo e viver uma vida simples.\nEm um lugar isolado, compra uma casinha rodeada de floresta.\nComeça então a viver sem tecnologia.','Apos um de seus banhos durante dia\nVocê descobre por acaso essa caverna, escura e fria\nCom muito medo e receio você começa a explorar esse novo local.']
    return frases[atual]

#   AUDIO DE CAMINHADA COM PRINT DE FRASE
def caminhando(cachoeira=True):
    opc = ['caminhando para a cachoeira .....','Caminhando para casa ....']
    if cachoeira:
        indice = 0
    else:
        indice = 1

    os.system('cls' if os.name == 'nt' else 'clear')
    audiJogo(1,True)
    for i in opc[indice]:
        print(f'{i}', end='', flush=True)
        sleep(0.1)
    audiJogo(0)

#   CACHOEIRA OPÇÃO
def opcoesDaCachoeira(opc):
    os.system('cls' if os.name == 'nt' else 'clear')
    if opc == '1':
        for i in 'Voce esta tomando um bom banho.....':
            print(f'{i}', end='', flush=True)
            sleep(0.1)
        chance = (randint(1,10))
        if chance == 7:
            for i in 'Olhando bem nas pedras atras da cachoeira\nVocê visualiza o que parece ser uma passagem para uma caverna ...':
                print(f'{i}', end='', flush=True)
                sleep(0.05)
            while True:
                choice = str(input('Deseja explorar a caverna ...\nSim ou Não - > ').lower().replace('ã','a'))
                if choice not in ['sim','nao','s','n']:
                    print('opção Invalida')
                elif choice in ['sim','s']:
                    print('Bem vindo a caverna')
                    sleep(1)
                    return True
                else:
                    print('Voltando ...')
                    sleep(1)
                    return False
    elif opc == '2':
        peixe = 0
        for i in 'Voce esta pescando.....':
            print(f'{i}', end='', flush=True)
            sleep(0.1)
        chance = (randint(1,10))
        if chance in [2,5]:
            peixe = 2
            print('Parabens você pegou 2 peixes.')
        elif chance in [1,3,7]:
            peixe = 1
            print('Você pegou 1 peixe')
        else:
            print('Infelizmente não foi dessa vez')
        sleep(1)
        return peixe
    