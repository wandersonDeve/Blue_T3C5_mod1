#01. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a,b,c):
    soma = a+b+c
    print(f'A soma dos 3 numeros foi de {soma}')

a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

soma(a,b,c)