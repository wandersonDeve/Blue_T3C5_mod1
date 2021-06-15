### 03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de acordo com o intervalo passado.

from time import sleep
print('=-'*17)
print('VAMOS FAZER UMA PROGRESSÃO')
print('=-'*17)
inicio = int(input('Digite o numero Inicial: '))
final = int(input('Digite o numero final: '))
razao = int(input('Agora, digite o passo: '))
sleep(0.5)
print('=-'*20)
print('Processando os dados inseridos',end='')
for i in range(0,8):
    print('.',end='',flush=True)
    sleep(0.5)
print()
print('Dados Processados\nMostrando resultado')
sleep(1)
print('=-'*20)
sleep(0.5)
if inicio < final:
    for i in range(inicio,final+1,razao):
        print(f'\033[01;33m{i}',end=' ',flush=True)
        sleep(0.2)
else:
    if razao > 0:
        razao = -razao
    for i in range(inicio,final-1,razao):
        print(f'\033[01;33m{i}',end=' ',flush=True)
        sleep(0.2)
sleep(0.5)
print('\033[m')
print('\033[01;31mFIM DO PROGRAMA\033[m')
print('=-'*20)