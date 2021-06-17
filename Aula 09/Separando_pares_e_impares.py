# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

numeros = []
pares = []
impares = []

while True:
    print('=-'*20)
    num = int(input('Digite um numero: ').strip())
    if num not in numeros:
        numeros.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    else:
        print('O numero digitado ja foi cadastrado')
    ctrl = str(input('Deseja continuar [S,N]\n --> ').strip().upper())
    if ctrl[0] == 'N':
        break

print(f'Os numeros digitados foram {sorted(numeros)}')
print(f'Os numeros pares são {sorted(pares)}')
print(f'Os numeros impares são {sorted(impares)}')