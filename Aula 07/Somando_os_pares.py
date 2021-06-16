#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

soma_par = total_par = 0

for i in range(1,7):
    num = int(input(f'Digite o {i}º numero interiro: ').strip().replace(',','.'))
    if num%2 == 0:
        soma_par += num
        total_par += 1

print(f'Foram digitados {total_par} valores pares e soma deles foi de {soma_par}')