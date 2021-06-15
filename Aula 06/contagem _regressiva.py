### 05 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('=-'*20)
print('Esta chegando a hora da queima de fogos\nVamos a contagem regressiva.....')
sleep(3)
print('=-'*20)
for i in range(10,-1,-1):
    print(i,end=' ',flush=True)
    sleep(1)
print()
print('shhhhhhhh, vuupt, pow, pow, pow')
print('=-'*20)