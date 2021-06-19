# 2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista,
# depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o
# programa. No final mostre:
# # Quantas pessoas foram cadastradas
# # Mostre a maior altura
# # Mostre a menor altura

cadastros = []

ctrl = 'S'
while ctrl != 'N':

    print('=-'*20)
    lista = [str(input('Qual o seu nome: ').strip()),float(input('Qual a sua altura em metros ').strip().replace(',','.'))]
    cadastros.append(lista)

    while True:
        controle = str(input('Deseja continuar inserindo dados? [N,S]: ').strip().upper())
        if controle in 'SN':
            ctrl = controle
            break

print('=-'*20)
print(f'Foram cadastradas {len(cadastros)} pessoas')

maior = menor = 0
for i in cadastros:
    if menor == 0 and maior == 0:
        menor = i[1]
        maior = i[1]
    if i[1] > maior:
        maior = i[1]
    if i[1] < menor:
        menor = i[1]
print(f'A maior altura foi de {maior} m')
print(f'A menor altura foi de {menor} m')
