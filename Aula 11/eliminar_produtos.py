### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos = {'coca':[15,4.00],'batata':[10,0.65],'pipoca':[4,2.25],'mostarda':[0,6.99],'pizza':[3,18]}
compras = {}

while True:
    print('=-'*30)

    item = str(input('Qual produto você deseja [SAIR para parar] : ').strip().lower())
    if item == 'sair':
        break
    valor_atual = print(produtos.get(item,'\033[1;31mProduto Inválido\033[m​​'))
    if item in produtos.keys():
        qtn_item = int(input(f'Quantos {item} você deseja: ').strip())

        if produtos[item][0] < qtn_item:
            print('Quantidade solicitada não disponível ')
        elif produtos[item][0]== 0:
            print('\033[1;31mProduto Indisponível\033[m​')
        else:
            print(f'\033[1;32mFoi adicionado no seu carrinho {qtn_item} {item}\033[m​​')
            compras[item] = qtn_item
            produtos[item][0] -= qtn_item
            print(produtos)
soma = 0
print('=-'*30)
print('\nSua lista de compras foi: ')
print('--'*30)
print(f"\033[1m{'Itens':<8}    {'Qtn':>3}   {'preço':>5}      {'Total':>5}\033[m")
print('--'*30)
for k,v in compras.items():
    print(f'{k.capitalize():<8} -> {v:>3} * {produtos[k][1]:>5.2f}  =  R$ {v*produtos[k][1]:>5.2f}')
    soma += v*produtos[k][1]
print('--'*30)
print(f'{"Total a pagar":<27} R$ {soma:>5.2f}\n\n')
