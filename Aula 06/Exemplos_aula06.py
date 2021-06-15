from time import sleep

nome = 'Wanderson'

for letra in nome:
    print(f'{letra}', end='',flush=True)
    sleep(0.2)
print()


lista = [10,20,30,40,50]
for i in range(0,len(lista)):
    print(f'{lista[i]}',end=',',flush=True)
    sleep(0.2)