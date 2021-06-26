#02.Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def validacao(a):
    if a == True:
        print('Verdadeiro')
    elif a == False:
        print('Falso')
    elif a == 0:
        print('0')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

print(f'{num1} é maior do que {num2}')
teste = num1 > num2
validacao(teste)