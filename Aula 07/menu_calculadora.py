# #01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
ctrl = 0
while ctrl != 5:
    choice = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n-> '))
    if choice == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif choice == 2:
        print(f'{num1} * {num2} = {num1*num2}')
    elif choice == 3:
        if num1 > num2:
            print(f'O numero {num1} é maior que o numero {num2}')
        else:
            print(f'O numero {num2} é maior que o numero {num1}')
    elif choice == 4:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))
    elif choice == 5:
        ctrl = 5
print('VOLTE LOGO')