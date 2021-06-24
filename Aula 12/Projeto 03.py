from datetime import date
from time import sleep

def validacao_ano_voto(pergunta):
    valor = 0
    while True:
        n = str(input(pergunta)).strip()
        if n.isnumeric():
            valor = int(n)
            if pergunta == 'Qual o ano de nascimento: ':
                if valor > date.today().year:
                    print(f'\033[1;33mHA HA HA HA HA, agora vamos fingir que vc é do futuro.\033[m')
                elif date.today().year - valor >= 120:
                    print(f'NOSSSSSA, Depois me passa a formula pra viver tanto assim.')
                    break
                else:
                    break
            else:
                break
        else:
            print(f'\033[1;31mERRO!!! \033[1;33m{n}\033[1;31m Não é valido como numero inteiro\033[m')
    return valor

def autoriza_voto(ano,voto):
    situacao = True
    idade = date.today().year - ano
    if 18 <= idade < 70:
        print('Voto OBRIGATÓRIO')
        situacao = True
    elif 16 <= idade < 18 or idade >= 70:
        print('Voto OPCIONAL')
        situacao = True
    else:
        print('Voto NEGADO')
        situacao = False
    votacao(situacao,voto)

def votacao(autorizacao,voto):
    if autorizacao:
        print('\033[1;32mSeu voto foi computado com sucesso.\033[m')
        
    else:
        print('\033[1;31mVocê ainda não tem idade para votar\033[m')

def continuar_votação(condição_de_parada):
    continuar = ''
    while True:
        resposta = str(input(condição_de_parada)).strip().replace('ã','a').capitalize()
        if resposta in ('Sim','Nao','S','N'):
            continuar = resposta[0]
        else:
            print('Valor de entrada invalido')
    return continuar

resultado = {}

while True:
    ano_nasci = validacao_ano_voto('Qual o ano de nascimento: ')
    voto_escolha = validacao_ano_voto('Qual o seu voto:\n\033[1;33m[ 1 ] - Joao\n[ 2 ] - Maria\n[ 3 ] - Jose\n[ 4 ] - Branco\033[m\nSeu voto é: ')
    autoriza_voto(ano_nasci,voto_escolha)

    ctrl = continuar_votação('Deseja continuar ? [N,S] ')
    if ctrl == 'N':
        break