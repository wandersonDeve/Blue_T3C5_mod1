#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

num = int(input('Digite um numero para ver a sua tabuada: '))
print('-='*10)
for i in range(1,11):
    print(f'{num:<3} x {i:>2} = {num*i:>4}')
print('-='*10)