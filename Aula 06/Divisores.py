### 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores
print('=-'*12)
print('DESCOBRINDO OS DIVISORES')
print('=-'*12)
while True:
    num = input('Digite um numero inteiro para descobrir seus divisores: ').strip()
    if num.isnumeric() == True and int(num) > 0:
        break
    else:
        print('\033[1;31mERRO!! Tente Novamente\033[m')
        print('=-'*12)

num_1 = int(num)
print(f'Os divisores de {num_1} são:',end=' ')
for i in range(1,num_1+1):
    if num_1 % i == 0:
        print(i,end=' ')
print()
print('=-'*12)
print('FIM DO PROGRAMA')