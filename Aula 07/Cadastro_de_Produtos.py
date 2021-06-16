# #03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = caro = barato = 0
nome = ''
ctrl = 'P'

while True:
    ctrl = 'N'
    print('=-'*20)
    item = str(input('Nome do Produto: '))
    valor = float(input('Valor do Iten: ').replace(',','.').strip())
    total += valor
    if valor > 1000:
        caro += 1
    if barato == 0 or valor < barato:
        barato = valor
        nome = item
    while ctrl != 'S':
       ctrl = str(input('Deseja Adicionar mais Itens: [S,N] ')).upper().strip()
       if ctrl == 'N':
         break
    if ctrl == 'N':
        break
print('\nO total gasto nessas compras foi de {:.2f}'
      '\nVocê comprou {} itens que custou mais de R$ 1000.00'
      '\nO produto mais barato foi a {}'.format(total,caro,nome))