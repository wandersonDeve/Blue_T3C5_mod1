#   IMPORTAÇÃO DAS BIBLIOTECAS NECESSARIAS PARA O PROGRAMA
from random import choice
from time import sleep
from stage_level import *
from emoji import emojize
import os

#   CLASSE QUE SERA RESPONSAVEL PELA HORA
class Relogio:
    def __init__(self):
        self.horas = 6
        self.__minutos = 0
        self.dia = 1
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self,novo_tempo):
        raise ValueError('Impossivel alterar o tempo dessa forma, use a função avancaTempo().')
    
    def avancaTempo(self, minutos):
        self.__minutos += minutos
        while self.__minutos >= 60:
            self.__minutos -= 60
            self.horas += 1
        while self.horas == 24:
            self.horas -= 24
            self.dia += 1
            personagem.dormiu = False

    
    def atrasado(self):
        return (self.horas > 12 or (self.horas == 12 and self.minutos > 0))

#   CLASSE QUE SERA RESPONSAVEL PELO PESONAGEM
class Personagem:
    def __init__(self):
        self.sujo = False # MODIFICAR ANTES DE ENVIAR
        self.fome = True
        self.lenha = False
        self.dinheiro = 3000 #### MODIFICAR VALOR NO FINAL DO CODIGO ####
        self.fase = 0
        self.banho = True
        self.viuMensagem = False
        self.cachoeira = False # essa opção seria para retornar uma ação dentro da cachoeira
        self.pescar = True
        self.dormiu = True
        self.vidas = 5
        self.aluguel = False
        self.teorAlcolico = 0
        self.bebado = False
        self.nivelCaverna = 0
    
    def __str__(self):
        return ("\033[1;31mVocê está sujo\033[m" if self.sujo else "\033[1;33mVocê está limpo\033[m")+", "+("\033[1;31mcom fome\033[m" if self.fome else "\033[1;33msem fome\033[m")+" e "+("\033[1;33mcortou lenha.\033[m" if self.lenha else "\033[1;31mnão cortou lenha.\033[m")

    #   FUNÇÃO PARA RETORNAR PADRÃO AS FUNÇÕES NO DIA SEGUINTE
    def dormir(self):
        self.sujo = True
        self.fome = True
        self.lenha = False
        self.pescar = True
        self.banho = True
        self.pescar = True
        self.dormiu = True
        self.teorAlcolico = 0
        self.bebado = False
        if 0 < relogio.horas < 6:
            pass
        else:
            relogio.dia += 1

    #   FUNÇÃO COM STATUS DO PERSONAGEM
    def status(self):
        print("---"*30)
        print(emojize(f':alarm_clock: {relogio}', use_aliases=True),end='    ')
        print(emojize(f':calendar: Dia {relogio.dia}', use_aliases=True),end='    ')
        print(emojize(f':dollar: R$ {personagem.dinheiro}', use_aliases=True), end='    ')
        print(emojize(f'Vidas: ' + '\033[1;31m:red_heart:\033[m '*personagem.vidas,use_aliases=True))
        print('==='*30)
        for k,v in casa.itens.items():
            if v != 0:
                print(emojize(f'{k} = {v}',use_aliases=True),end='  ')
        print('\n'+'==='*30)
        print("Você precisa cortar lenha antes das 12hs.")
        print(personagem)
        print("--"*20)

#   CLASSE QUE MOSTRA O QUE TEM EM SUA DISPENSA
class Casa:
    def __init__(self):
        self.itens = {':flashlight:':1,':knot:':0,':fish:':1,':hook:':0,':wood:':2,':coin:':0,':curry:':0,':chopsticks:':0}

#   AÇÕES DO USUARIO
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()

    #   INTRODUÇÃO DA HISTORIA
    # audiJogo(0,True)
    # msg = atualStage(personagem.fase)
    # for i in msg:
    #     print(f'{i}', end='',flush=True)
    #     sleep(0.05)
    # audiJogo(0)
    # personagem.viuMensagem = True
    # sleep(1)
    # os.system('cls' if os.name == 'nt' else 'clear')

    #   REPETIÇÃO DAS AÇÕES UTILZADAS PELO USUARIO
    while True:
        dia_controle = 1
        if dia_controle != relogio.dia and personagem.aluguel == True:
            personagem.dinheiro -= 200
            dia_controle = relogio.dia

        if personagem.vidas == 0:
            print('\033[1;31mVOCÊ PERDEU\033[m, INICIE NOVAMENTE E COMECE UMA NOVA AVENTURA')
            break
        personagem.status()
        print("Ações:")
        opcao = input('1 - Ir para Cachoeira\n2 - Fritar Peixe\n3 - Ir para cidade\n4 - Comer\n' + ('5 - Cortar lenha' if personagem.lenha == False else '\033[1;31mDesabilitado por hoje\033[m') + ('\n\033[1;31mDesabilitado\033[m' if 6 <= relogio.horas <= 16 else '\n6 - Dormir') + '\n0 - Sair do jogo\nEscolha sua ação: ')

        #   OPÇÃO DA CACHOEIRA
        if opcao == '1':
            relogio.avancaTempo(20)

            # REPETIÇÃO DE ATOS NA CACHOEIRA
            caminhando()
            audiJogo(2,True)
            opc = ''
            while opc != '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                personagem.status()
                opc = input(('1 - Tomar banho\n' if personagem.banho else '\033[1;31mO banho esta desabilitada por enquanto\033[m\n') + ('2 - Pescar' if personagem.pescar else '\033[1;31mA pescaria esta desabilitada por hoje\033[m') + '\n3 - Voltar para casa\nEscolha sua ação: ')
                if opc == '1' and personagem.banho == True:
                    casa.itens,personagem = opcoesDaCachoeira(casa.itens,personagem,opc)
                    personagem.sujo = False
                    personagem.banho = False
                    relogio.avancaTempo(20)
                elif opc == '2' and personagem.pescar == True:
                    casa.itens,personagem = opcoesDaCachoeira(casa.itens,personagem,opc)
                    personagem.pescar = False
                    relogio.avancaTempo(20)
                elif opc == '3':
                    relogio.avancaTempo(20)
                    audiJogo(0)
                    opn = '3'
                    caminhando(False)
                else:
                    print("Opção inválida!")
                    relogio.avancaTempo(5)

        #   OPÇÃO DE PREPARAR A COMIDA
        elif opcao == '2':
            print("Você tem peixe e lenha\nPreparando sua comida" if casa.itens[':fish:'] > 0 and casa.itens[':wood:'] >= 2 else "Você ou não tem peixe ou não tem lenha suficiente")
            if casa.itens[':fish:'] > 0 and casa.itens[':wood:'] >= 2:
                casa.itens[':fish:'] -= 1
                casa.itens[':wood:'] -= 2
                casa.itens[':curry:'] += 1
            relogio.avancaTempo(30)
            sleep(2)
    
        #   OPÇÃO DE IR PARA CIDADE
        elif opcao == '3':
            casa.itens,personagem = cidade(casa.itens,personagem)
            relogio.avancaTempo(180)

        #   OPÇÃO ONDE ELE COME O ALIMENTO PREPARADO
        elif opcao == '4':
            if casa.itens[':curry:'] > 0:
                personagem.fome = False
                casa.itens[':curry:'] -= 1
                relogio.avancaTempo(15)
                print('Você comeu e esta bem alimentado')
            else:
                print("Não tem comida na sua casa.")
                relogio.avancaTempo(5)
            sleep(1)

        #   AÇÕES QUANDO O USUARIO ESCOLHER CORTAR A LENHA
        elif opcao == '5' and personagem.lenha == False:
            print("-=-=-")
            print("Você foi cortar madeira.")
            print(personagem)
            print("-=-=-")
            lenha = randint(4,10)
            if not personagem.dormiu:
                print("Como você não dormiu, acabou pegando no sono antes de cortar a lenha.")
                lenha = 0
            elif personagem.bebado:
                print('Você estava muito bebado e não produziu nada, e nem se lembra de como voltou para casa')
                lenha = 0
                personagem.dormir()
            elif personagem.sujo:
                print("Como você estava sujo, e acabou atraindo a atenção de alguns animais que nao deixaram você cortar a madeira")
                lenha = 0
            elif personagem.fome:
                print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
                lenha = randint(0,3)
            elif relogio.atrasado():
                print("Como você chegou atrasado, você produziu menos do que de costume.")
                lenha = (randint(4,10)//2)
            print(f'Você produziu {lenha} lenhas hoje')
            print("-=-=-")
            sleep(3)
            relogio.avancaTempo(360)
            casa.itens[':wood:'] += lenha
            personagem.banho = True
            personagem.sujo = True
            personagem.lenha = True

            # OPÇÃO QUANDO UM COMPRADOR APARECER
            comprador = randint(1,4)
            if comprador == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                vender = randint(1,5)
                valor = choice([20,30,40])
                comprar = True
                while comprar:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==='*30)
                    for k,v in casa.itens.items():
                        if v != 0:
                            print(emojize(f'{k} = {v}',use_aliases=True),end='  ')
                    print('\n'+'==='*30)
                    print('Uma pessoa da cidade esta a sua procura e quer comprar lenha....')
                    escolha = input(f'Deseja vender {vender} lenha\n1 - Vender\n2 - Não vender\nEscolha sua ação: ')
                    if escolha == '1' and casa.itens[':wood:'] >= vender:
                        print(f'Você vender {vender} a {valor:.2f} cada e recebeu {vender*valor:.2f}')
                        casa.itens[':wood:'] -= vender
                        personagem.dinheiro += vender*valor
                        sleep(2)
                        comprar = False
                    elif escolha == '2':
                        print('O comprador foi embora....')
                        sleep(1)
                        comprar = False
                    else:
                        print('Parece que digitou uma opção invalida ou não tem lenha o suficiente para vender')
                        sleep(2)
    
        #   DORMIR
        elif opcao == '6':
            personagem.dormir()

        #   OPÇÃO DE SAIR DO PROGRAMA
        elif opcao == '0':
            break
    
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

print('Jogo produzido por:\nDanusa\nNilson\nVinicius\nWanderson')