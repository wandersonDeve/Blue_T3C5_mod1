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
        self.minutos = 0
        self.dia = 1
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while self.minutos >= 60:
            self.minutos -= 60
            self.horas += 1
        while self.horas >= 24:
            self.horas -= 24
            self.dia += 1

    
    def atrasado(self):
        return (self.horas > 12 or (self.horas == 12 and self.minutos > 0))

#   CLASSE QUE SERA RESPONSAVEL PELO PESONAGEM
class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.lenha = False
        self.dinheiro = 0
        self.fase = 0
        self.banho = True
        self.viuMensagem = False
        self.cachoeira = False # essa opção seria para retornar uma ação dentro da cachoeira
        self.pescar = True
        self.dormiu = True
    
    def __str__(self):
        return ("\033[1;31mVocê está sujo\033[m" if self.sujo else "\033[1;33mVocê está limpo\033[m")+", "+("\033[1;31mcom fome\033[m" if self.fome else "\033[1;33msem fome\033[m")+" e "+("\033[1;33mcortou lenha.\033[m" if self.lenha else "\033[1;31mnão cortou lenha.\033[m")

    #   FUNÇÃO PARA RETORNAR PADRÃO AS FUNÇÕES NO DIA SEGUINTE
    def dormir(self):
        self.sujo = True
        self.fome = True
        self.lenha = False
        self.pescar = True
        self.banho = True
        self.cachoeira = False # essa opção seria para retornar uma ação dentro da cachoeira
        self.pescar = True
        self.dormiu = True   

    #   FUNÇÃO COM STATUS DO PERSONAGEM
    def status(self):
        print("--"*20)
        print(emojize(f':alarm_clock: {relogio}', use_aliases=True),end='    ')
        print(emojize(f':calendar: Dia {relogio.dia}', use_aliases=True),end='    ')
        print(emojize(f':dollar: R$ {personagem.dinheiro}', use_aliases=True))
        print(casa.itens)
        print("--"*20)
        print("Você precisa cortar lenha antes das 12hs.")
        print(personagem)
        print("--"*20)

#   CLASSE QUE MOSTRA O QUE TEM EM SUA DISPENSA
class Casa:
    def __init__(self):
        self.itens = {'lanterna':0,'corda':0,'peixe':1,'gancho':0,'lenha':2,'ouro':0,'comida':0}

#   AÇÕES DO USUARIO
if __name__ == "__main__":
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()

    #   INTRODUÇÃO DA HISTORIA
    # stage_level.audiJogo(0,True)
    # msg = atualStage(personagem.fase)
    # for i in msg:
    #     print(f'{i}', end='',flush=True)
    #     sleep(0.1)
    # stage_level.audiJogo(0)
    # personagem.viuMensagem = True
    # sleep(1)
    # os.system('cls' if os.name == 'nt' else 'clear')

    #   REPETIÇÃO DAS AÇÕES UTILZADAS PELO USUARIO
    while True:
        personagem.status()
        print("Ações:")
        opcao = input('1 - Ir para Cachoeira\n2 - Fritar Peixe\n4 - Comer\n' + ('7 - Cortar lenha' if personagem.lenha == False else 'Desabilitado por hoje') + '\n0 - Sair do jogo\nEscolha sua ação: ')
        if opcao == "1":
            relogio.avancaTempo(20)

            # REPETIÇÃO DE ATOS NA CACHOEIRA
            opn = ''
            caminhando()
            audiJogo(2,True)
            while opn != '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                personagem.status()
                opc = input(('1 - Tomar banho\n' if personagem.banho else '\033[1;31mO banho esta desabilitada por enquanto\033[m\n') + ('2 - Pescar' if personagem.pescar else '\033[1;31mA pescaria esta desabilitada por hoje\033[m') + '\n3 - Voltar para casa\nEscolha sua ação: ')
                if opc == '1' and personagem.banho == True:
                    personagem.cachoeira = opcoesDaCachoeira(opc)
                    personagem.sujo = False
                    personagem.banho = False
                    relogio.avancaTempo(20)
                elif opc == '2' and personagem.pescar == True:
                    casa.itens['peixe'] += opcoesDaCachoeira(opc)
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
        elif opcao == "2":
            print("Você tem peixe e lenha\nPreparando sua comida" if casa.itens['peixe'] > 0 and casa.itens['lenha'] >= 2 else "Você ou não tem peixe ou não tem lenha suficiente")
            if casa.itens['peixe'] > 0 and casa.itens['lenha'] >= 2:
                casa.itens['peixe'] -= 1
                casa.itens['lenha'] -= 2
                casa.itens['comida'] += 1
            relogio.avancaTempo(30)
            sleep(3)
       
        # elif opcao == "3" :
        #     if personagem.dinheiro >= 15:
        #         personagem.dinheiro -= 15
        #         cafe_da_manha = True
        #     else:
        #         print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
        #     relogio.avancaTempo(5)

        #   OPÇÃO ONDE ELE COME O ALIMENTO PREPARADO
        elif opcao == "4":
            if casa.itens['comida'] > 0:
                personagem.fome = False
                casa.itens['comida'] -= 1
                relogio.avancaTempo(15)
                print('Você comeu e esta bem alimentado')
            else:
                print("Não tem comida na sua casa.")
                relogio.avancaTempo(5)
            sleep(1)
       
        # elif opcao == "5":
        #     if casa.remedios > 0:
        #         casa.remedios -= 1
        #         personagem.medicado = True
        #     else:
        #         print("Não tem remédio na sua casa")
        #     relogio.avancaTempo(5)

        # elif opcao == "6":
        #     if personagem.dinheiro >= 20:
        #         casa.remedios += 10
        #         personagem.dinheiro -= 20
        #         relogio.avancaTempo(10)
        #     else:
        #         print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
        #         relogio.avancaTempo(5)

        #   AÇÕES QUANDO O USUARIO ESCOLHER CORTAR A LENHA
        elif opcao == "7" and personagem.lenha == False:
            print("-=-=-")
            print("Você foi cortar madeira.")
            print(personagem)
            print("-=-=-")
            lenha = randint(4,10)
            if not personagem.dormiu:
                print("Como você não dormiu, acabou pegando no sono antes de cortar a lenha.")
                lenha = 0
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
            casa.itens['lenha'] += lenha
            personagem.banho = True
            personagem.sujo = True
            personagem.lenha = True

            # OPÇÃO QUANDO UM COMPRADOR APARECER
            comprador = 2
            if comprador == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                vender = randint(1,5)
                valor = choice([20,30,40])
                print(casa.itens)
                comprar = True
                while comprar:
                    print('Uma pessoa da cidade esta a sua procura e quer comprar lenha....')
                    escolha = input(f'Deseja vender {vender} lenha\n1 - Vender\n2 - Não vender\nEscolha sua ação: ')
                    if escolha == '1':
                        print(f'Você vender {vender} a {valor:.2f} cada e recebeu {vender*valor:.2f}')
                        casa.itens['lenha'] -= vender
                        personagem.dinheiro += vender*valor
                        sleep(2)
                        comprar = False
                    elif escolha == '2':
                        print('O comprador foi embora....')
                        sleep(1)
                        comprar = False
                    else:
                        pass
            # personagem.dinheiro += recebido
            # personagem.dormir()
            # relogio = Relogio()
            # dia+=1
       
        #   OPÇÃO DE SAIR DO PROGRAMA
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')