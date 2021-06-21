# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.

cadastrados = []
maior = menor = 0

for i in range(0,5):
    lista = []
    print('=-'*20)
    lista.append(str(input('Qual seu nome: ').strip()))
    lista.append(int(input('Qual sua idade: ').strip()))
    cadastrados.append(lista)
 
print('=-'*20)
for i in cadastrados:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade')
        maior += 1
    else:
        print(f'{i[0]} é menor de idade')
        menor += 1
print(f'O total de pessoas com mais maior de idade {maior} e menores foi de {menor}')