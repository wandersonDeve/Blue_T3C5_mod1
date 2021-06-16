#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = menor = 0

for i in range(1,6):
    wei = float(input(f'Digite o peso da {i}ª pessoa: ').strip().replace(',','.'))
    if peso == menor == 0:
        peso = wei
        menor = wei
    if peso < wei:
        peso = wei
    if menor > wei:
        menor = wei

print(f'O maior peso foi {peso}\nO menor peso foi {menor}')