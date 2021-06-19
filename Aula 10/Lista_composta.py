# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.

cadastrados = []

for i in range(0,5):
    lista = []
    print('=-'*20)
    nome = str(input('Qual seu nome: ').strip())
    idade = int(input('Qual sua idade: ').strip())
    lista.append(nome)
    lista.append(idade)
    cadastrados.append(lista)
 
print('=-'*20)
for i in cadastrados:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade')
    else:
        print(f'{i[0]} é menor de idade')