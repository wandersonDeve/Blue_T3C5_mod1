from datetime import date
from time import sleep

def validacao_ano_voto(pergunta):
    '''
    :Função validacao_ano_voto: Valida se o ano e o voto é um numero inteiro
    :varialvel valor: Varialvel com o valor passado pelo usuario convertido em numero inteiro
    :while: Laço para repetir a pergunta, caso a resposta passada seja invalida
    :varialvel n: Varialvel com o valor passado pelo usuario como String
    :param pergunta: Usa uma pergunta enviada por parametro, para o usuario
    :return: retorna um numero inteiro
    '''
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
    '''
    :param ano: ano de nascimento do usuario
    :param voto: opção de voto do usuario
    :return: retorna se o usuario esta apto para votar
    '''
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
    '''
    :param autorizacao: Fornece valor Booleano para a validação do voto
    :param voto: opção do voto do usuario
    :return: ---- sem retorno ----
    '''
    if voto > 4:
        indice = 4
    else:
        indice = voto-1

    if autorizacao:
        resultado[indice]['votos'] += 1
        print('\033[1;32mSeu voto foi computado com sucesso.\033[m')  
    else:
        print('\033[1;31mVocê ainda não tem idade para votar\033[m')

def continuar_votacao(condição_de_parada):
    '''
    :param condição_de_parada: Condição para parar de aceitar novas pessoas para votar
    :return: retorna S = sim e N = não, para o programa
    '''
    continuar = ''
    while True:
        resposta = str(input(condição_de_parada)).strip().replace('ã','a').capitalize()
        if resposta in ('Sim','Nao','S','N'):
            continuar = resposta[0]
            break
        else:
            print('Valor de entrada invalido')
    return continuar

resultado = [{'nome':'Joao','votos':0},{'nome':'Maria','votos':0},{'nome':'Jose','votos':0},{'nome':'Branco','votos':0},{'nome':'Nulo','votos':0}]

while True:
    ano_nasci = validacao_ano_voto('Qual o ano de nascimento: ')
    voto_escolha = validacao_ano_voto('Qual o seu voto:\n\033[1;33m[ 1 ] - Joao\n[ 2 ] - Maria\n[ 3 ] - Jose\n[ 4 ] - Branco\033[m\nSeu voto é: ')
    autoriza_voto(ano_nasci,voto_escolha)

    ctrl = continuar_votacao('Deseja continuar ? [N,S] ')
    if ctrl == 'N':
        break

total_votos = 0
vencedor = ''

print(f"{'Candidato':<10}{'Votos':>5}")
for i in resultado:
    print(f"{i['nome']:<10}{i['votos']:>4}")
    if i > 3 :
        if i['votos'] > total_votos:
            total_votos = i['votos']
            vencedor = i['nome']

print(f'O candidato vencedor com {total_votos} votos foi ', end='')
for i in range(0,7):
    print('.',end=' ')
print(f'{vencedor.upper()}')