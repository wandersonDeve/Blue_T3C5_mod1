#06.Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def maior_menor(num1,num2):
    if num1 < num2:
        print(f'O numero {num1} é menor que {num2}')
    elif num2 < num1:
        print(f'O numero {num2} é menor que {num1}')
    else:
        print(f'Os numeros {num1} são iguais')

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

maior_menor(n1,n2)