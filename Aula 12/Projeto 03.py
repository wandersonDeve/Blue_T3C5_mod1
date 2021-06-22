
from datetime import date

joao = maria = jose = 0

#def validacao_numero():

def autoriza_voto(ano,voto):
    idade = date.today().year - ano
    if idade >= 18:
        return votacao(True,voto)
    else:
        return votacao(False,voto)

def votacao(autorizacao,voto):
    if autorizacao:
        print('\033[1;32mSeu voto foi computado com sucesso.\033[m')
    else:
        print('\033[1;31mVocê ainda não pode votar, voto cancelado\033[m')


while True:
    ano_nasci = int(input('Qual o ano de nascimento: '))
    voto_escolha = str(input('Qual o seu voto:\n\033[1;33mJoao\nMaria\nJose\033[m\nSeu voto é: ').lower())
    autoriza_voto(ano_nasci,voto_escolha)
    
    ctrl = str(input('Deseja continuar ? [N,S] ').upper())
    if ctrl == 'N':
        break

