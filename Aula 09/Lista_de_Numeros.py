# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

numeros = []
while True:
    print('=-'*20)
    num = int(input('Digite um numero: ').strip())
    if num not in numeros:
        numeros.append(num)
    else:
        print('O numero digitado ja foi cadastrado')
    ctrl = str(input('Deseja continuar [S,N]\n --> ').strip().upper())
    if ctrl[0] == 'N':
        break

print(sorted(numeros))