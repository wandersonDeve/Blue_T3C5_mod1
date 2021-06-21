import random


print("***********Bem vindo ao jokenpo!**********")
cont = int(input('Digite a quantidade de jogos!'))
possib_maquina = ["Pedra","Papel","Tesoura"]
jogada_player =  ["Pedra","Papel","Tesoura"]
jogada_maquina = random.choice(possib_maquina)
Contagem_player = 0
Contagem_Maquina = 0
print(jogada_maquina)
while cont > 0:
    jogada_player = input('Qual sua jogada? Pedra, Papel ou Tesoura?').capitalize()
    if jogada_player == jogada_maquina:
        print("Draw!")
        cont -= 1
    elif jogada_player == "Pedra" and jogada_maquina == "Papel":
        print('Papel embrulha pedra!')
        print('Vitoria da maquina!')
        Contagem_Maquina += 1
        cont -= 1
    elif jogada_player == "Pedra" and jogada_maquina == "Tesoura":
        print('Pedra quebra tesoura!')
        print('Vitória do player!')
        Contagem_player += 1
        cont -= 1
    elif jogada_player == "Tesoura" and jogada_maquina == "Papel":
        print('Tesoura corta o papel!')
        print('Vitória do player!')
        Contagem_player += 1
        cont -= 1
    elif jogada_player == "Tesoura" and jogada_maquina == "Pedra":
        print('Pedra quebra a tesoura!')
        print('Vitoria da maquina!')
        Contagem_Maquina += 1
        cont -= 1
    elif jogada_player == "Papel" and jogada_maquina == "Tesoura":
        print('A tesoura corta o papel!')
        print('Vitoria da maquina!')
        Contagem_Maquina += 1
        cont -= 1
    elif jogada_player == "Papel" and jogada_player == "Pedra":
        print('Papel embrulha a pedra!')
        print('Vitória do player!')
        Contagem_player += 1
        cont -= 1
    
print('Fim do jogo!!')       
print(f'O jogador tem {Contagem_player} pontos!')
print(f'A maquina tem {Contagem_Maquina} pontos!')