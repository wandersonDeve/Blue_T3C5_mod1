from pygame import mixer
from time import sleep
from random import randint,choice
from emoji import emojize
import os

def status_pesonagem(inventario):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('==='*30)
    for k,v in inventario.items():
        if v != 0:
            print(emojize(f'{k} = {v}',use_aliases=True),end='  ')
    print('\n'+'==='*30)


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

#   FUNÇÃO PARA A FUTURA LOJA DO PERSONAGEM
def loja_Vazia(inventario,personagem):
    aluguel_loja = 200
    while True:
        status_pesonagem(inventario)
        print(f'Esta loja esta disponivel para alugar por {aluguel_loja} o dia')
        print('Ações')
        print('1 - alugar')
        print('2 - sair')
        opcao = input('escolha sua ação: ')
        if opcao == '1':
            if personagem.dinheiro < aluguel_loja:
                print('voce nao tem dinheiro sufisciente para alugar')
            elif opcao == '1':
                personagem.aluguel = True
        elif opcao == '2':
            return inventario,personagem
        else:
            print('\033[1;31mOpção Inválida\033[m')

#   FUNÇÃO COM A OPÇÃO DA MERCEARIA
def mercearia(inventario,personagem):
    if personagem.sujo or personagem.bebado == True:
        print('Você foi expulso do bar, porque esta fedendo de mais')
        sleep(2)
    else:
        itens = {':flashlight:':1,':hook:':3, ':knot:':2}
        valores = [400,700,600]
        print('Ola, gostaria de comprar algo?')
        sleep(1)
        while True:
            index = 0
            status_pesonagem(inventario)
            print('Digite o numero do item que deseja comprar, ou digite "sair", para deixar a loja: ')
            print(f"{'Numero':<6}   {'Item':<4} {'Quantidade':<15}{'Valor':<6}")
            for k,v in itens.items():
                print(emojize(f'{index+1:<6}   {k:<4} {v:<15}{valores[index]:<6.2f}',use_aliases=True ))
                index += 1
            opcao = input('opção: ').lower().strip()
            if opcao == '1':
                if personagem.dinheiro < valores[0]:
                    print('Voce nao tem',valores[0], 'para comprar esse item')
                else:
                    print('Compra efetuada com sucesso.\nVocê adquiriu uma Lanterna')
                    inventario[':flashlight:'] += 1
                    personagem.dinheiro -= valores[0]
            elif opcao == '2':
                if personagem.dinheiro < valores[1]:
                    print('Voce nao tem',valores[1], 'para comprar esse item')
                else:
                    print('Compra efetuada com sucesso.\nVocê adquiriu uma Gancho')
                    inventario[':hook:'] += 1
                    personagem.dinheiro -= valores[1]
            elif opcao == '3':
                if personagem.dinheiro < valores[2]:
                    print('Voce nao tem',valores[2], 'para comprar esse item')
                else:
                    print('Compra efetuada com sucesso.\nVocê adquiriu uma Corda')
                    inventario[':knot:'] += 1
                    personagem.dinheiro -= valores[2]
            elif opcao == 'sair':
                return inventario,personagem
            else:
                print('\033[1;31mOpção Invalida\033[m')

#   FUNÇÃO COM A OPÇÃO DO BAR
def bar(inventario,personagem):
    if personagem.sujo or personagem.bebado == True:
        print('Você foi expulso do bar, porque esta fedendo de mais')
        sleep(2)
    else:
        teor_alcol = personagem.teorAlcolico
        print ('Bem-Vindo ao Bar:')
        sleep(1)
        while True:
            status_pesonagem(inventario)
            print("Ações:")
            print("1 - Beber")
            print("2 - voltar para a cidade")
            print("")
            opcao = input("Escolha sua ação: ")
            if opcao == '1':
                personagem.dinheiro -= 30
                bebida = randint(2,10)
                teor_alcol += bebida
                if 40 < teor_alcol < 90:
                    cena1 = randint(1,30)
                    if cena1 == 3:
                        print('Um homem totalmente embrigado esbarra em voce')
                        print()
                        print("1 - fazer ele pedir desculpas")
                        print("2 - deixa por isso mesmo, afinal ele esta embriagado")
                        acao = input('Escolha sua Ação: ')
                        if acao == '1':
                            cena2 = randint(1,5)
                            if cena2 == 2:
                                print ('O homem nao quis se desculpar e lhe agrediu, para seu azar ele é ex lutador de MMA, Morreu perdeu uma vida')
                                personagem.vida -= 1
                            else:
                                print('O homem pediu desculpas e ainda pagou uma bebida para voce ')
                                teor_alcol += randint(2,10)
                        elif acao == '2':
                            print('Sábia escolha')
                        else:
                            print('\033[1;31mOpção invalida\033[m')
            elif opcao == '2':
                if teor_alcol > 90:
                    personagem.bebado = True
                return inventario,personagem

#   FUNÇÃO COM A OPÇÃO DE APOSTA EM CAVALOS
def hipodromo(inventario,personagem):
    if personagem.sujo or personagem.bebado == True:
        print('Você foi expulso Hipodromo, porque esta fedendo de mais')
        sleep(2)
        return inventario,personagem
    else:
        cavalos = ['Galã','Relâmpago','Sargento','Bandolero','Duquesa','Pé De Pano'] ##lista com nomes do cavalo
        print ('Bem-Vindo a corrida de cavalos:')
        sleep(1)
        while True:
            status_pesonagem(inventario)
            print("")
            print("Ações:")
            print("1 - Apostar em uma corrida")
            print("2 - voltar para a cidade")
            opcao = input("Escolha sua ação: ")
            if opcao == '1':
                for i in cavalos:  ##printar a lista de opcoes de aposta
                    print(f'[{i}]',end= ' ')
                print()
                aposta = input(f'Em qual cavalo deseja apostar? (digite corretamente o nome do cavalo) ').title().strip()
                quantia = int(input('qual quantia deseja apostar?\/ Maximo de \033[1;32m{personagem.dinheiro}\033[m\n'))
                if quantia <= personagem.dinheiro:
                    vencedor = choice(cavalos) ## escolhe por aleatoriedade do cavalo vencedor
                    print(f'O cavalo vencedor foi {vencedor}')
                    if aposta == vencedor: ## validacao do vencedor
                        quantia = quantia * (len(cavalos)-1) 
                        personagem.dinheiro += quantia
                        print (f'\033[1;33mParabens, voce ganhou {quantia}\033[m')
                        sleep(1)
                    else:
                        print('\033[1;31mVoce perdeu a aposta\033[m')
                        personagem.dinheiro -= quantia
                        sleep(1)
                else:
                    print('Você não tem dinheiro suficiente para fazer essa aposta')
            elif opcao == '2':
                return inventario,personagem
            else:
                print('\033[1;31Entrada invalida\033[m')
                sleep(1)

#   FUNÇÃO QUE MOSTRA AS OPÇÕES QUE A PESSOA TEM NO RESTAURANTE
def restaurante(inventario,personagem):
    if personagem.sujo == True or personagem.bebado == True:
        print('Você foi expulso do Restaurante, porque esta fedendo de mais')
        sleep(2)
        return inventario,personagem
    else:
        print('Voce entrou no restaurante')
        while True:
            status_pesonagem(inventario)
            print("Ações:")
            print("1 - Pedir comida")
            print("2 - Vender seu peixe para o restaurante")
            print("3 - Sair do restaurante")
            opcao = input("Escolha sua ação: ")
            if opcao == '1':
                if personagem.dinheiro >= 80:
                    personagem.fome = False
                    personagem.dinheiro -= 80 
                else:
                    print('Você não tem dinheiro sufuciente, o valor é de R$ 80,00')     
            if opcao == '2':
                opcao = int(input('Quantos peixes quer vender?: '))
                preco = randint(10,30)
                print('Voce vendeu', opcao, 'peixes, pelo valor de', preco,'a unidade')
                valor = opcao * preco
                personagem.dinheiro += valor  
                inventario[':fish:'] -= opcao   
            elif opcao == '3':
                return inventario,personagem
            else:
                print('\033[1;31Entrada invalida\033[m')
                sleep(1)

#   FUNÇÃO QUE MOSTRA AS OPÇÕES QUE A PESSOA TEM NA CIDADE
def cidade(dict,pessoa):
    inventario = dict
    personagem = pessoa
    while True: ### opcoes do que fazer na cidade
        status_pesonagem(inventario)
        print()
        print("Voce esta na Cidade")
        print("Ações:")
        print("1 - Restaurante")
        print("2 - Corrida de cavalos")
        print("3 - Bar")
        print("4 - Mercearia")
        print("5 - Loja vazia")
        print("6 voltar para casa")
        opcao = input("Escolha sua ação: ")

        if opcao == '1':
            inventario,personagem = restaurante(inventario,personagem) ## condicao para ir no restaurante
        elif opcao == '2':
            inventario,personagem = hipodromo(inventario,personagem) ##condicao para ir na corrida
        
        elif opcao == '3': ## condicao para ir ao bar
            inventario,personagem = bar(inventario,personagem)

        elif opcao == '4':
            inventario,personagem = mercearia(inventario,personagem)

        elif opcao == '5':
            inventario,personagem = loja_Vazia(inventario,personagem)
        
        elif opcao == '6':
            return inventario, personagem
        else:
            print('\033[1;31Entrada invalida\033[m')
            sleep(1)