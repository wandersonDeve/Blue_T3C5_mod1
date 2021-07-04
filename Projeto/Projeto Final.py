#   IMPORTAÇÃO DAS BIBLIOTECAS NECESSARIAS PARA O PROGRAMA
from time import sleep
import stage_level
from emoji import emojize
import os

#   CLASSE QUE SERA RESPONSAVEL PELA HORA
class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

#   CLASSE QUE SERA RESPONSAVEL PELO PESONAGEM
class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100
        self.fase = 0
        self.viuMensagem = False
        self.cachoeira = False
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"cortou lenha."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False

    #   FUNÇÃO COM STATUS DO PERONAGEM
    def status(self):
        print("--"*20)
        print(emojize(f':alarm_clock: {relogio}', use_aliases=True),end='    ')
        print(emojize(f':calendar: Dia {dia}', use_aliases=True),end='    ')
        print(emojize(f':dollar: R$ {personagem.dinheiro}', use_aliases=True))
        print("--"*20)
        print("Você precisa cortar lenha antes das 17hs.")
        print(personagem)
        print("--"*20)

#   CLASSE QUE MOSTRA O QUE TEM EM SUA DISPENSA
class Casa:
    def __init__(self):
        self.remedios = 1
        self.comida = 5

#   AÇÕES DO USUARIO
if __name__ == "__main__":
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    cafe_da_manha = False

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
        opcao = input("1 - Ir para Cachoeira\n0 - Sair do jogo\nEscolha sua ação: ")
        if opcao == "1":
            relogio.avancaTempo(20)

            # REPETIÇÃO DE ATOS NA CACHOEIRA
            opn = ''
            stage_level.caminhando()
            stage_level.audiJogo(2,True)
            while opn != '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                personagem.status()
                opc = input("1 - Tomar Banho\n2 - Pescar\n3 - Voltar para casa\nEscolha sua ação: ")
                if opcao == '1':
                    personagem.cachoeira = stage_level.opcoesDaCachoeira(opc)
                    personagem.sujo = False
                    relogio.avancaTempo(20)
                    opn = '3'
                elif opcao == "2":
                    
                    relogio.avancaTempo(20)
                elif opcao == "3":
                    relogio.avancaTempo(20)
                    stage_level.audiJogo(0)
                    stage_level.caminhando(False)
                    opn = '3'
                else:
                    print("Opção inválida!")
                    relogio.avancaTempo(5)

        # elif opcao == "2":
        #     if casa.comida > 0:
        #         casa.comida -= 1
        #         cafe_da_manha = True
        #     else:
        #         print("Não há comida em casa.")
        #     relogio.avancaTempo(15)
        # elif opcao == "3" :
        #     if personagem.dinheiro >= 15:
        #         personagem.dinheiro -= 15
        #         cafe_da_manha = True
        #     else:
        #         print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
        #     relogio.avancaTempo(5)
        # elif opcao == "4":
        #     if cafe_da_manha:
        #         personagem.fome = False
        #         cafe_da_manha = False
        #         relogio.avancaTempo(15)
        #     else:
        #         print("Não tem café da manhã na sua casa.")
        #         relogio.avancaTempo(5)
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
        # elif opcao == "7":
        #     print("-=-=-")
        #     print("Você foi trabalhar.")
        #     print(personagem)
        #     print("-=-=-")
        #     recebido = personagem.salario
        #     if not personagem.medicado:
        #         print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
        #         recebido = 0
        #     elif personagem.sujo:
        #         print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
        #         recebido *= 0.9
        #     elif personagem.fome:
        #         print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
        #         recebido *= 0.5
        #     elif relogio.atrasado():
        #         print("Como você chegou atrasado, você produziu menos do que de costume.")
        #         recebido *= 0.8
        #     print("Você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
        #     print("-=-=-")
        #     sleep(3)

            # personagem.dinheiro += recebido
            # personagem.dormir()
            # relogio = Relogio()
            # dia+=1
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')